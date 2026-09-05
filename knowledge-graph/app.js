/* 知识学习路线图前端（v6）：roadmap.sh/machine-learning 结构式布局。
 * 垂直主脊线自上而下穿过模块芯片；每个阶段顶部是深色里程碑横条（含进度）；
 * 知识点芯片在右侧按行排列，细灰连接线从模块引出；直接关联用绿色虚线弧。
 * 无力学模拟，确定性布局；数据来自 data.js（无外部依赖，可离线打开）。
 */
(function () {
  'use strict'

  const data = window.KB_DATA
  const nodes = data.nodes.map(function (n) {
    return Object.assign({}, n, { visible: true, dim: 1 })
  })
  const byId = new Map(nodes.map(function (n) { return [n.id, n] }))
  const pointById = new Map(data.points.map(function (p) { return [p.id, p] }))
  const moduleById = new Map(data.modules.map(function (m) { return [m.id, m] }))
  const stageByCode = new Map(data.stages.map(function (s) { return [s.code, s] }))
  const relOf = new Map()
  for (const e of data.related) {
    if (!relOf.has(e.source)) relOf.set(e.source, [])
    if (!relOf.has(e.target)) relOf.set(e.target, [])
    relOf.get(e.source).push(e)
    relOf.get(e.target).push(e)
  }
  const pathIdx = new Map()
  data.path.forEach(function (id, i) { pathIdx.set(id, i) })
  const related = data.related.filter(function (e) {
    return pointById.has(e.source) && pointById.has(e.target)
  })

  // ---- roadmap.sh 风格配色：阶段色 = 由浅入深的黄→橙系列 ----
  const STAGE_RAMP = [
    { bg: '#fde047', border: '#ca8a04', text: '#713f12' }, // 0 浅黄
    { bg: '#f59e0b', border: '#b45309', text: '#ffffff' }, // 1 橙黄
    { bg: '#ea580c', border: '#9a3412', text: '#ffffff' }, // 2 橙
    { bg: '#c2410c', border: '#7c2d12', text: '#ffffff' }, // 3 深橙
    { bg: '#9a3412', border: '#7c2d12', text: '#ffffff' }, // 4
    { bg: '#7c2d12', border: '#431407', text: '#ffffff' }, // 5
  ]
  const FUTURE_COLOR = '#94a3b8'
  function rampOf(code) {
    const i = Number(code)
    return STAGE_RAMP[isNaN(i) ? STAGE_RAMP.length - 1 : Math.min(i, STAGE_RAMP.length - 1)]
  }
  const colorOf = function (code) { return code === 'future' ? FUTURE_COLOR : rampOf(code).border }
  const bgOf = function (code) { return code === 'future' ? FUTURE_COLOR : rampOf(code).bg }
  const textOf = function (code) { return code === 'future' ? '#ffffff' : rampOf(code).text }
  const C = {
    ink: '#0f172a', sub: '#64748b',
    canvas: '#ffffff', grid: '#eceef1',
    connector: '#e2e6ea', plannedEdge: '#cbd2d9',
    related: '#10b981', chipBg: '#ffffff',
    border: '#e9ebee', done: '#10b981', hover: 'rgba(37,99,235,.4)',
    milestone: '#1f2937',
  }

  // ---- 布局常量（roadmap.sh 式，紧凑排布） ----
  const SPINE_X = 175
  const AREA_X = 300
  const SLOT_W = 140, SLOT_H = 46, MAXC = 4
  const WORLD_W = AREA_X + MAXC * SLOT_W + 70

  const canvas = document.getElementById('canvas')
  const ctx = canvas.getContext('2d')
  const wrap = document.getElementById('stage-wrap')
  const holder = document.getElementById('canvas-holder')
  const detailEl = document.getElementById('detail')
  const tooltip = document.createElement('div')
  tooltip.id = 'tt'
  wrap.appendChild(tooltip)

  const view = { x: 0, y: 0, scale: 1 }
  let layout = null
  let selected = null
  let hovered = null
  let hoverChip = null
  let focusModule = null
  let preFocusView = null   // 进入聚焦前的视口，退出时还原
  let panning = false
  let panMoved = false
  let lastPos = null

  // ---------- 布局 ----------
  function measureTrunc(text, font, maxW) {
    ctx.font = font
    let s = String(text)
    while (s.length > 1 && ctx.measureText(s).width > maxW) {
      s = s.slice(0, s.length - 2) + '…'
    }
    return s
  }

  // 按像素宽度折行，最多 maxLines 行；放不下的末行仍截断（长知识点名完整显示）
  function wrapText(text, font, maxW, maxLines) {
    ctx.font = font
    const full = String(text)
    if (maxLines < 2 || ctx.measureText(full).width <= maxW) {
      return [full]
    }
    const lines = []
    let rest = full
    while (lines.length < maxLines - 1 && rest.length > 1) {
      let cut = rest.length
      while (cut > 1 && ctx.measureText(rest.slice(0, cut)).width > maxW) cut--
      lines.push(rest.slice(0, cut))
      rest = rest.slice(cut)
    }
    lines.push(measureTrunc(rest, font, maxW))
    return lines
  }

  function computeLayout() {
    const milestones = []
    const bands = []
    const plannedChips = []
    const posBy = new Map()   // id -> {x, y, w, h}
    let y = 44

    function milestone(s) {
      const m = { node: byId.get('s:' + s.code), x: 40, y: y, w: WORLD_W - 80, h: 50 }
      milestones.push(m)
      posBy.set(m.node.id, { x: m.x, y: m.y, w: m.w, h: m.h })
      y += 50 + 16
    }

    for (const s of data.stages) {
      milestone(s)
      for (const md of data.modules.filter(function (m) { return m.stage === s.code })) {
        const modNode = byId.get(md.id)
        const pts = (md.points || []).map(function (id) { return byId.get(id) }).filter(Boolean)
        const kn = Math.max(1, pts.length)
        const cols = Math.min(MAXC, Math.max(1, Math.ceil(kn / Math.ceil(kn / MAXC))))
        const rows = Math.ceil(kn / cols)
        const bandH = Math.max(44, rows * SLOT_H + 6)
        const modFont = '600 14px "Inter","SF Pro Text","Segoe UI","PingFang SC","Microsoft YaHei",sans-serif'
        const modText = measureTrunc(md.code + ' ' + md.name, modFont, 190)
        ctx.font = modFont
        const modW = ctx.measureText(modText).width + 30
        const modChip = { node: modNode, x: SPINE_X - modW / 2, y: y + bandH / 2 - 18, w: modW, h: 36 }
        posBy.set(md.id, { x: modChip.x, y: modChip.y, w: modW, h: 36 })
        const chips = []
        const chipFont = '12px "Inter","SF Pro Text","Segoe UI","PingFang SC","Microsoft YaHei",sans-serif'
        pts.forEach(function (p, i) {
          const r = Math.floor(i / cols)
          const c = i % cols
          const cx = AREA_X + c * SLOT_W + SLOT_W / 2
          const cy = y + 3 + r * SLOT_H + SLOT_H / 2
          const lines = wrapText(p.name, chipFont, p.learned ? 100 : 104, 2)
          ctx.font = chipFont
          let textW = 0
          for (const l of lines) textW = Math.max(textW, ctx.measureText(l).width)
          const w = textW + (p.learned ? 26 : 22)
          const chipH = lines.length > 1 ? 42 : 30
          const chip = { node: p, x: cx - w / 2, y: cy - chipH / 2, w: w, h: chipH, lines: lines }
          chips.push(chip)
          posBy.set(p.id, { x: chip.x, y: chip.y, w: w, h: chipH })
        })
        bands.push({ mod: md, modChip: modChip, chips: chips, y: y, h: bandH })
        y += bandH + 10
      }
      const pls = data.planned.filter(function (p) { return p.stage === s.code })
      if (pls.length) {
        pls.forEach(function (p, i) {
          const pn = byId.get(p.id)
          const font = '10.5px "Inter","SF Pro Text","Segoe UI","PingFang SC","Microsoft YaHei",sans-serif'
          const text = measureTrunc(p.name, font, 140)
          ctx.font = font
          const w = ctx.measureText(text).width + 20
          const chip = { node: pn, x: AREA_X + i * 150 + SLOT_W / 2 - w / 2, y: y + 14, w: w, h: 28 }
          plannedChips.push(chip)
          posBy.set(p.id, { x: chip.x, y: chip.y, w: w, h: 28 })
        })
        y += 40
      }
      y += 8
    }
    // 未来规划里程碑 + 规划芯片
    const futurePl = data.planned.filter(function (p) { return p.stage === null })
    if (futurePl.length) {
      let fnode = byId.get('s:future')
      if (!fnode) {
        fnode = { id: 's:future', type: 'future', code: 'future', name: '🔜 未来规划', progress: null }
        nodes.push(fnode)
        byId.set(fnode.id, fnode)
      }
      const m = { node: fnode, x: 40, y: y, w: WORLD_W - 80, h: 50 }
      milestones.push(m)
      posBy.set(fnode.id, { x: m.x, y: m.y, w: m.w, h: m.h })
      y += 50 + 16
      futurePl.forEach(function (p, i) {
        const pn = byId.get(p.id)
        const font = '10.5px "Inter","SF Pro Text","Segoe UI","PingFang SC","Microsoft YaHei",sans-serif'
        const text = measureTrunc(p.name, font, 140)
        ctx.font = font
        const w = ctx.measureText(text).width + 20
        const chip = { node: pn, x: AREA_X + i * 150 + SLOT_W / 2 - w / 2, y: y + 14, w: w, h: 28 }
        plannedChips.push(chip)
        posBy.set(p.id, { x: chip.x, y: chip.y, w: w, h: 28 })
      })
      y += 40
    }

    layout = {
      milestones: milestones, bands: bands, plannedChips: plannedChips,
      posBy: posBy, worldW: WORLD_W, worldH: y + 70,
    }
  }

  // ---------- 渲染 ----------
  function resize() {
    const dpr = window.devicePixelRatio || 1
    canvas.width = holder.clientWidth * dpr
    canvas.height = holder.clientHeight * dpr
    canvas.style.width = holder.clientWidth + 'px'
    canvas.style.height = holder.clientHeight + 'px'
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
  }

  function focusSet() {
    const s = new Set()
    if (focusModule) {
      const m = focusModule
      s.add(m.id)
      const st = byId.get('s:' + m.stage)
      if (st) s.add(st.id)
      const md = moduleById.get(m.id)
      for (const id of (md ? md.points : [])) {
        s.add(id)
        for (const e of (relOf.get(id) || [])) {
          s.add(e.source); s.add(e.target)
        }
      }
    } else {
      const focus = hovered || selected
      if (focus) {
        s.add(focus.id)
        for (const e of (relOf.get(focus.id) || [])) {
          s.add(e.source); s.add(e.target)
        }
        if (focus.type === 'knowledge' && focus.module) s.add('m:' + focus.module)
        if (focus.type === 'module') {
          const md = moduleById.get(focus.id)
          for (const id of (md ? md.points : [])) s.add(id)
        }
      }
    }
    return s
  }

  function elAlpha(node, fs, hasFocus) {
    if (!node.visible) return 0
    if (focusModule) return fs.has(node.id) ? 1 : 0.05
    if (!hasFocus) return node.dim
    return fs.has(node.id) ? 1 : 0.1
  }

  function render() {
    ctx.clearRect(0, 0, holder.clientWidth, holder.clientHeight)
    ctx.save()
    ctx.translate(holder.clientWidth / 2 + view.x, holder.clientHeight / 2 + view.y)
    ctx.scale(view.scale, view.scale)

    // 点阵网格
    const gs = 46
    const wl = (-holder.clientWidth / 2 - view.x) / view.scale
    const wt = (-holder.clientHeight / 2 - view.y) / view.scale
    const wr = holder.clientWidth / view.scale
    const wb = holder.clientHeight / view.scale
    ctx.fillStyle = C.grid
    for (let gx = Math.floor(wl / gs) * gs; gx < wl + wr + gs; gx += gs) {
      for (let gy = Math.floor(wt / gs) * gs; gy < wt + wb + gs; gy += gs) {
        ctx.fillRect(gx, gy, 2, 2)
      }
    }

    const fs = focusSet()
    const hasFocus = hovered !== null || selected !== null
    ctx.lineCap = 'round'

    // 主脊线（穿过模块芯片的垂直粗线，底部箭头 = 学习方向向下）
    ctx.strokeStyle = C.connector
    ctx.lineWidth = 2.2
    ctx.beginPath()
    ctx.moveTo(SPINE_X, layout.milestones[0].y + layout.milestones[0].h)
    ctx.lineTo(SPINE_X, layout.worldH - 52)
    ctx.stroke()
    ctx.fillStyle = C.connector
    ctx.beginPath()
    ctx.moveTo(SPINE_X, layout.worldH - 44)
    ctx.lineTo(SPINE_X - 5, layout.worldH - 54)
    ctx.lineTo(SPINE_X + 5, layout.worldH - 54)
    ctx.closePath()
    ctx.fill()

    // 阶段里程碑横条（由浅入深的阶段色系列）
    for (const m of layout.milestones) {
      const alpha = elAlpha(m.node, fs, hasFocus)
      if (alpha <= 0.01) continue
      ctx.globalAlpha = Math.max(alpha, focusModule ? 0.22 : alpha)
      const col = bgOf(m.node.code)
      const colText = textOf(m.node.code)
      const colEdge = colorOf(m.node.code)
      ctx.fillStyle = col
      ctx.beginPath()
      ctx.roundRect(m.x, m.y, m.w, m.h, 10)
      ctx.fill()
      ctx.fillStyle = colEdge
      ctx.beginPath()
      ctx.roundRect(m.x + 1.5, m.y + 12, 5, m.h - 24, 3)
      ctx.fill()
      ctx.fillStyle = colText
      ctx.font = '600 16.5px "Inter","SF Pro Text","Segoe UI","PingFang SC","Microsoft YaHei",sans-serif'
      ctx.textAlign = 'left'
      ctx.textBaseline = 'middle'
      ctx.fillText(m.node.name, m.x + 18, m.y + m.h / 2 + 0.5)
      if (m.node.progress !== null && m.node.progress !== undefined) {
        const bw = 120
        const bx = m.x + m.w - bw - 68
        ctx.fillStyle = colText + '40'
        ctx.beginPath()
        ctx.roundRect(bx, m.y + m.h / 2 - 4.5, bw, 9, 4.5)
        ctx.fill()
        ctx.fillStyle = colText
        ctx.beginPath()
        ctx.roundRect(bx, m.y + m.h / 2 - 4.5, Math.max(5, bw * Math.min(100, m.node.progress) / 100), 9, 4.5)
        ctx.fill()
        ctx.font = '600 12px "Inter","SF Pro Text","Segoe UI","PingFang SC","Microsoft YaHei",sans-serif'
        ctx.textAlign = 'left'
        ctx.fillText(m.node.progress + '%', bx + bw + 10, m.y + m.h / 2 + 0.5)
      }
    }

    // 模块 -> 知识点 连接线（阶段色粗线 + 箭头，与周围芯片配色一致）
    for (const band of layout.bands) {
      const mc = band.modChip
      const modAlpha = elAlpha(mc.node, fs, hasFocus)
      const stemX = Math.max(AREA_X - 26, mc.x + mc.w + 12)
      const lineColor = colorOf(mc.node.stage)
      for (const chip of band.chips) {
        const a = Math.min(modAlpha, elAlpha(chip.node, fs, hasFocus))
        if (a <= 0.01) continue
        ctx.globalAlpha = a * 0.85
        ctx.strokeStyle = lineColor
        ctx.lineWidth = 2
        ctx.beginPath()
        ctx.moveTo(mc.x + mc.w, mc.y + mc.h / 2)
        ctx.lineTo(stemX, mc.y + mc.h / 2)
        ctx.lineTo(stemX, chip.y + chip.h / 2)
        ctx.lineTo(chip.x - 7, chip.y + chip.h / 2)
        ctx.stroke()
        // 箭头（指向知识点芯片）
        const ax = chip.x - 7
        const ay = chip.y + chip.h / 2
        ctx.fillStyle = lineColor
        ctx.beginPath()
        ctx.moveTo(ax, ay)
        ctx.lineTo(ax - 7, ay - 4.5)
        ctx.lineTo(ax - 7, ay + 4.5)
        ctx.closePath()
        ctx.fill()
      }
    }

    // 直接关联（绿色虚线弧，向右弓起）
    for (const e of related) {
      const pa = layout.posBy.get(e.source)
      const pb = layout.posBy.get(e.target)
      if (!pa || !pb) continue
      const na = byId.get(e.source)
      const nb = byId.get(e.target)
      const a = elAlpha(na, fs, hasFocus)
      const b = elAlpha(nb, fs, hasFocus)
      if (a <= 0.01 || b <= 0.01) continue
      const hi = fs.has(e.source) && fs.has(e.target)
      ctx.globalAlpha = (focusModule ? (hi ? 1 : 0.04) : (hasFocus ? (hi ? 1 : 0.06) : 0.9)) * Math.min(a, b)
      const ax = pa.x + pa.w
      const ay = pa.y + pa.h / 2
      const bx = pb.x + pb.w
      const by = pb.y + pb.h / 2
      const cx = Math.max(ax, bx) + 60
      const cy = (ay + by) / 2
      ctx.strokeStyle = C.related
      ctx.lineWidth = hi ? 2.8 : 2.2
      ctx.setLineDash([6, 4])
      ctx.beginPath()
      ctx.moveTo(ax, ay)
      ctx.quadraticCurveTo(cx, cy, bx, by)
      ctx.stroke()
      ctx.setLineDash([])
      if (e.label) {
        const t = 0.5, mt = 1 - t
        const qx = mt * mt * ax + 2 * mt * t * cx + t * t * bx
        const qy = mt * mt * ay + 2 * mt * t * cy + t * t * by
        ctx.font = '10.5px "Inter","SF Pro Text","Segoe UI","PingFang SC","Microsoft YaHei",sans-serif'
        const w = ctx.measureText(e.label).width + 12
        const chip = { x: qx - w / 2, y: qy - 8.5, w: w, h: 17, edge: e }
        e._chip = chip
        ctx.fillStyle = C.chipBg
        ctx.strokeStyle = C.related
        ctx.lineWidth = 1
        ctx.beginPath()
        ctx.roundRect(chip.x, chip.y, chip.w, chip.h, 9)
        ctx.fill()
        ctx.stroke()
        ctx.fillStyle = '#047857'
        ctx.textAlign = 'center'
        ctx.textBaseline = 'middle'
        ctx.fillText(e.label, chip.x + chip.w / 2, chip.y + chip.h / 2 + 0.5)
      }
    }

    // 模块芯片
    for (const band of layout.bands) {
      const mc = band.modChip
      const alpha = elAlpha(mc.node, fs, hasFocus)
      if (alpha <= 0.01) continue
      ctx.globalAlpha = alpha
      drawChip(mc, {
        fill: C.chipBg, stroke: colorOf(mc.node.stage), lw: 1.5, radius: 9,
        text: mc.node.code + ' ' + mc.node.name, font: '600 14px "Inter","SF Pro Text","Segoe UI","PingFang SC","Microsoft YaHei",sans-serif',
        textColor: C.ink, maxW: 190, pad: 30,
      })
    }

    // 知识点芯片
    for (const band of layout.bands) {
      for (const chip of band.chips) {
        const alpha = elAlpha(chip.node, fs, hasFocus)
        if (alpha <= 0.01) continue
        ctx.globalAlpha = alpha
        const p = chip.node
        const col = colorOf(p.stage)
        drawChip(chip, {
          fill: C.chipBg, stroke: p.learned ? col : '#cbd2d9',
          lw: p.learned ? 1.4 : 1.1, radius: 7, dashed: !p.learned,
          text: p.name, font: '12px "Inter","SF Pro Text","Segoe UI","PingFang SC","Microsoft YaHei",sans-serif',
          textColor: p.learned ? C.ink : C.sub, maxW: p.learned ? 100 : 104,
          pad: p.learned ? 26 : 22, learned: p.learned, textShift: p.learned ? 4 : 0,
        })
      }
    }

    // 规划芯片
    for (const chip of layout.plannedChips) {
      const alpha = elAlpha(chip.node, fs, hasFocus)
      if (alpha <= 0.01) continue
      ctx.globalAlpha = alpha
      drawChip(chip, {
        fill: C.chipBg, stroke: '#cbd2d9', lw: 1.1, radius: 7, dashed: true,
        text: chip.node.name, font: '10.5px "Inter","SF Pro Text","Segoe UI","PingFang SC","Microsoft YaHei",sans-serif',
        textColor: C.sub, maxW: 140, pad: 20,
      })
    }

    ctx.globalAlpha = 1
    ctx.restore()
  }

  function drawChip(rect, o) {
    const isSel = selected && selected.id === rect.node.id
    const isHov = hovered && hovered.id === rect.node.id
    // 芯片尺寸按文字重新量取，保证与布局一致；rect.lines 存在则多行绘制（知识点完整显示）
    ctx.font = o.font
    const lines = rect.lines || [measureTrunc(rect.node.name, o.font, o.maxW)]
    let textW = 0
    for (const l of lines) textW = Math.max(textW, ctx.measureText(l).width)
    const w = textW + o.pad
    rect.x = rect.x + rect.w / 2 - w / 2
    rect.w = w
    if (isHov || isSel) {
      ctx.strokeStyle = C.hover
      ctx.lineWidth = 2.5
      ctx.beginPath()
      ctx.roundRect(rect.x - 4, rect.y - 4, w + 8, rect.h + 8, o.radius + 4)
      ctx.stroke()
    }
    ctx.beginPath()
    ctx.roundRect(rect.x, rect.y, w, rect.h, o.radius)
    ctx.fillStyle = o.fill
    ctx.fill()
    ctx.strokeStyle = o.stroke
    ctx.lineWidth = o.lw
    if (o.dashed) ctx.setLineDash([4, 3])
    ctx.stroke()
    ctx.setLineDash([])
    if (o.learned) {
      ctx.fillStyle = C.done
      ctx.beginPath()
      ctx.arc(rect.x + 11, rect.y + rect.h / 2, 2.5, 0, Math.PI * 2)
      ctx.fill()
    }
    ctx.fillStyle = o.textColor
    ctx.font = o.font
    ctx.textAlign = 'center'
    ctx.textBaseline = 'middle'
    const lh = 14  // 多行行距
    const y0 = rect.y + rect.h / 2 - (lines.length - 1) * lh / 2 + 0.5
    for (let i = 0; i < lines.length; i++) {
      ctx.fillText(lines[i], rect.x + w / 2 + (o.textShift || 0), y0 + i * lh)
    }
  }

  function fitView() {
    const w = layout.worldW
    const h = layout.worldH
    view.scale = Math.min((holder.clientWidth - 320) / w, (holder.clientHeight - 60) / h, 1.15)
    view.x = -(w / 2) * view.scale
    view.y = -(h / 2) * view.scale
    render()
  }

  function fitToVisible() {
    const rects = []
    for (const m of layout.milestones) if (m.node.visible) rects.push(m)
    for (const b of layout.bands) {
      if (!b.modChip.node.visible) continue
      rects.push(b.modChip)
      for (const c of b.chips) if (c.node.visible) rects.push(c)
    }
    for (const c of layout.plannedChips) if (c.node.visible) rects.push(c)
    if (!rects.length) return
    let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity
    for (const r of rects) {
      minX = Math.min(minX, r.x); maxX = Math.max(maxX, r.x + r.w)
      minY = Math.min(minY, r.y); maxY = Math.max(maxY, r.y + r.h)
    }
    const w = Math.max(60, maxX - minX)
    const h = Math.max(60, maxY - minY)
    view.scale = Math.min((holder.clientWidth - 320) / w, (holder.clientHeight - 60) / h, 1.15)
    view.x = -(minX + maxX) / 2 * view.scale
    view.y = -(minY + maxY) / 2 * view.scale
    render()
  }

  function animateTo(ts, tx, ty, dur) {
    const s0 = view.scale, x0 = view.x, y0 = view.y
    const t0 = performance.now()
    function tick(now) {
      let t = Math.min(1, (now - t0) / dur)
      t = 1 - Math.pow(1 - t, 3)
      view.scale = s0 + (ts - s0) * t
      view.x = x0 + (tx - x0) * t
      view.y = y0 + (ty - y0) * t
      render()
      if (t < 1) requestAnimationFrame(tick)
    }
    requestAnimationFrame(tick)
  }

  function focusViewTo(modNode) {
    const md = moduleById.get(modNode.id)
    if (!md) return
    const ids = [modNode.id]
    for (const id of md.points) {
      ids.push(id)
      for (const e of (relOf.get(id) || [])) ids.push(e.source, e.target)
    }
    ids.push('s:' + modNode.stage)
    const rects = []
    for (const id of ids) {
      const r = layout.posBy.get(id)
      if (r) rects.push(r)
    }
    if (!rects.length) return
    let minX = Infinity, maxX = -Infinity, minY = Infinity, maxY = -Infinity
    for (const r of rects) {
      minX = Math.min(minX, r.x - 20); maxX = Math.max(maxX, r.x + r.w + 20)
      minY = Math.min(minY, r.y - 20); maxY = Math.max(maxY, r.y + r.h + 20)
    }
    const w = Math.max(80, maxX - minX)
    const h = Math.max(80, maxY - minY)
    const ts = Math.min((holder.clientWidth - 320) / w, (holder.clientHeight - 60) / h, 1.35)
    const tx = -(minX + maxX) / 2 * ts
    const ty = -(minY + maxY) / 2 * ts
    animateTo(ts, tx, ty, 300)
  }

  // ---------- 交互 ----------
  function screenToWorld(sx, sy) {
    return {
      x: (sx - holder.clientWidth / 2 - view.x) / view.scale,
      y: (sy - holder.clientHeight / 2 - view.y) / view.scale,
    }
  }

  function hitRect(wx, wy) {
    const all = layout.milestones.concat(
      layout.bands.map(function (b) { return b.modChip }),
      layout.bands.reduce(function (acc, b) { return acc.concat(b.chips) }, []),
      layout.plannedChips,
    )
    for (let i = all.length - 1; i >= 0; i--) {
      const r = all[i]
      const node = r.node
      if (!node.visible) continue
      if (wx >= r.x - 4 && wx <= r.x + r.w + 4 && wy >= r.y - 4 && wy <= r.y + r.h + 4) return node
    }
    return null
  }

  function hitChipRect(wx, wy) {
    for (const e of related) {
      if (!e._chip) continue
      const c = e._chip
      if (wx >= c.x && wx <= c.x + c.w && wy >= c.y && wy <= c.y + c.h) return e
    }
    return null
  }

  canvas.addEventListener('pointerdown', function (ev) {
    panning = true
    panMoved = false
    lastPos = { x: ev.clientX, y: ev.clientY }
    canvas.setPointerCapture(ev.pointerId)
  })
  canvas.addEventListener('pointermove', function (ev) {
    const rect = canvas.getBoundingClientRect()
    const sx = ev.clientX - rect.left
    const sy = ev.clientY - rect.top
    if (panning && lastPos) {
      if (Math.hypot(ev.clientX - lastPos.x, ev.clientY - lastPos.y) > 4) panMoved = true
      view.x += ev.clientX - lastPos.x
      view.y += ev.clientY - lastPos.y
      lastPos = { x: ev.clientX, y: ev.clientY }
      render()
      return
    }
    const p = screenToWorld(sx, sy)
    const n = hitRect(p.x, p.y)
    const chip = hitChipRect(p.x, p.y)
    if (n !== hovered || chip !== hoverChip) {
      hovered = n
      hoverChip = chip
      canvas.style.cursor = n ? 'pointer' : (chip ? 'help' : 'grab')
      if (chip) {
        const a = byId.get(chip.source)
        const b = byId.get(chip.target)
        tooltip.innerHTML = '<b>' + esc(a.name) + ' ↔ ' + esc(b.name) + '</b>' +
          (chip.label ? ' <span style="color:#047857">· ' + esc(chip.label) + '</span>' : '')
        tooltip.style.display = 'block'
        tooltip.style.left = Math.min(ev.clientX + 14, window.innerWidth - 260) + 'px'
        tooltip.style.top = (ev.clientY + 14) + 'px'
      } else if (n) {
        tooltip.innerHTML = nodeTip(n)
        tooltip.style.display = 'block'
        tooltip.style.left = Math.min(ev.clientX + 14, window.innerWidth - 260) + 'px'
        tooltip.style.top = (ev.clientY + 14) + 'px'
      } else {
        tooltip.style.display = 'none'
      }
      render()
    } else if (chip || n) {
      tooltip.style.left = Math.min(ev.clientX + 14, window.innerWidth - 260) + 'px'
      tooltip.style.top = (ev.clientY + 14) + 'px'
    }
  })
  canvas.addEventListener('pointerup', function (ev) {
    panning = false
    if (!panMoved) {
      const rect = canvas.getBoundingClientRect()
      const p = screenToWorld(ev.clientX - rect.left, ev.clientY - rect.top)
      const n = hitRect(p.x, p.y)
      if (n) {
        if (n.type === 'module') {
          if (focusModule === n) {
            focusModule = null
            restoreFocusView()
          } else {
            preFocusView = { scale: view.scale, x: view.x, y: view.y }
            focusModule = n
            focusViewTo(n)
          }
        }
        openDetail(n)
      } else {
        focusModule = null
        restoreFocusView()
      }
    }
    lastPos = null
  })
  function restoreFocusView() {
    if (preFocusView) {
      animateTo(preFocusView.scale, preFocusView.x, preFocusView.y, 260)
      preFocusView = null
    }
  }
  window.addEventListener('keydown', function (ev) {
    if (ev.key === 'Escape') {
      focusModule = null
      selected = null
      restoreFocusView()
      showPlaceholder()
      render()
    }
  })
  canvas.addEventListener('wheel', function (ev) {
    ev.preventDefault()
    const rect = canvas.getBoundingClientRect()
    const sx = ev.clientX - rect.left
    const sy = ev.clientY - rect.top
    const factor = ev.deltaY < 0 ? 1.1 : 0.9
    const ns = Math.min(3, Math.max(0.2, view.scale * factor))
    const wx = (sx - holder.clientWidth / 2 - view.x) / view.scale
    const wy = (sy - holder.clientHeight / 2 - view.y) / view.scale
    view.scale = ns
    view.x = sx - holder.clientWidth / 2 - wx * ns
    view.y = sy - holder.clientHeight / 2 - wy * ns
    render()
  }, { passive: false })

  // ---------- 详情面板 ----------
  function esc(s) {
    return String(s == null ? '' : s)
      .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
  }

  function showPlaceholder() {
    const s = data.stats
    let learned = 0
    for (const p of data.points) if (p.learned) learned++
    detailEl.innerHTML =
      '<div class="placeholder">' +
      '<div class="ph-title">📌 节点详情</div>' +
      '<p>点击左侧任意节点查看具体介绍：</p>' +
      '<p style="margin-top:6px">· <b>知识点芯片</b> — 说明 / 直接关联 / 相关踩坑 / 学习日志</p>' +
      '<p>· <b>模块芯片</b> — 本节全部知识点清单</p>' +
      '<p>· <b>阶段里程碑</b> — 学习进度与包含模块</p>' +
      '<div class="ph-tip">📊 当前共 ' + s.knowledge + ' 个知识点（已学 ' + learned + ' / 未学 ' +
      (s.knowledge - learned) + '）<br>' +
      '🔗 直接关联 ' + s.related + ' 条 · 🕳 踩坑 ' + s.pitfalls + ' 个<br>' +
      '🖱 悬停芯片可快速预览说明</div>' +
      '</div>'
  }

  function nodeTip(n) {
    if (n.type === 'knowledge') {
      return '<b>' + esc(n.name) + '</b>' +
        (n.learned ? ' <span style="color:#059669">✅</span>' : ' <span style="color:#94a3b8">⏳</span>') +
        '<div style="color:#64748b;margin-top:3px">' + esc(n.desc || '') + '</div>' +
        '<div style="color:#94a3b8;font-size:10.5px;margin-top:3px">' + esc(n.module) + ' · ' +
        (n.learned ? '已学' : '未学') + '</div>'
    }
    if (n.type === 'module') {
      return '<b>' + esc(n.name) + '</b>' +
        '<div style="color:#64748b;margin-top:3px">点击查看本节全部知识点 · 聚焦该节</div>'
    }
    if (n.type === 'stage' || n.type === 'future') {
      return '<b>' + esc(n.name) + '</b>' +
        (n.progress != null
          ? '<div style="color:#64748b;margin-top:3px">学习进度 ' + n.progress + '%</div>'
          : '<div style="color:#64748b;margin-top:3px">尚未开始</div>')
    }
    return '<b>' + esc(n.name) + '</b><div style="color:#64748b;margin-top:3px">规划中</div>'
  }

  function pointLink(p) {
    return '<a class="link" data-point="' + esc(p.id) + '">' + esc(p.name) + '</a>'
  }

  function moduleLink(m) {
    return '<a class="link" data-module="' + esc(m.id) + '">' + esc(m.code + ' ' + m.name) + '</a>'
  }

  function openDetail(n) {
    selected = n
    let html = '<button class="close" id="detail-close">✕</button>'
    if (n.type === 'knowledge') {
      const m = moduleById.get('m:' + n.module)
      html += '<span class="badge" style="background:' + colorOf(n.stage) + '">知识点 · ' + esc(n.module) + '</span>' +
        '<h2>' + esc(n.name) + '</h2>' +
        '<div class="meta">' + (n.learned ? '✅ 已学' : '⏳ 未学') + ' · ' + esc(n.desc) + '</div>'
      if (m) {
        html += '<div class="block"><h3>所属模块</h3><ul><li>' + moduleLink(m) + '</li></ul></div>'
      }
      const rels = relOf.get(n.id) || []
      if (rels.length) {
        html += '<div class="block"><h3>直接关联</h3><ul>' +
          rels.map(function (e) {
            const other = e.source === n.id ? pointById.get(e.target) : pointById.get(e.source)
            return '<li>' + pointLink(other) +
              (e.label ? ' <span style="color:#047857">· ' + esc(e.label) + '</span>' : '') + '</li>'
          }).join('') + '</ul></div>'
      }
      if (n.pitfalls && n.pitfalls.length) {
        html += '<div class="block"><h3>相关踩坑</h3><ul>' +
          n.pitfalls.map(function (p) {
            return '<li>🕳 <b>坑' + p.num + '</b> ' + esc(p.err) +
              ' <span style="color:#94a3b8">→ ' + esc(p.fix) + '</span></li>'
          }).join('') + '</ul></div>'
      }
      if (n.days && n.days.length) {
        const dayMap = new Map(data.days.map(function (d) { return [d.num, d] }))
        html += '<div class="block"><h3>学习日志</h3><ul>' +
          n.days.map(function (num) {
            const d = dayMap.get(num)
            if (!d) return ''
            return '<li><a class="link" href="../logs/day-' + String(num).padStart(2, '0') + '.md" target="_blank">📝 Day ' + num +
              (d.date ? '（' + esc(d.date) + '）' : '') + ' ' + esc(d.title || '') + ' ↗</a></li>'
          }).join('') + '</ul></div>'
      }
      const idx = pathIdx.get(n.id)
      const pre = idx > 0 ? byId.get(data.path[idx - 1]) : null
      const nxt = idx >= 0 && idx < data.path.length - 1 ? byId.get(data.path[idx + 1]) : null
      if (pre || nxt) {
        html += '<div class="block"><h3>学习路径位置</h3><ul>' +
          (pre ? '<li>⬅ 前置：' + pointLink(pre) + '</li>' : '') +
          (nxt ? '<li>➡ 后继：' + pointLink(nxt) + '</li>' : '') +
          '</ul></div>'
      }
    } else if (n.type === 'module') {
      const md = moduleById.get(n.id)
      const pitfalls = []
      let learnedCount = 0
      for (const id of (md ? md.points : [])) {
        const p = pointById.get(id)
        if (p) {
          if (p.learned) learnedCount++
          for (const pf of (p.pitfalls || [])) pitfalls.push(pf)
        }
      }
      html += '<span class="badge" style="background:' + colorOf(n.stage) + '">模块 ' + esc(n.code) + '</span>' +
        '<h2>' + esc(n.name) + '</h2>' +
        '<div class="meta">已学 ' + learnedCount + '/' + (md ? md.points.length : 0) +
        ' · ' + pitfalls.length + ' 相关踩坑</div>' +
        '<div class="block"><h3>核心知识点</h3><ul>' +
        (md ? md.points : []).map(function (id) {
          const p = pointById.get(id)
          return p ? '<li>' + pointLink(p) + (p.learned ? ' ✅' : ' ⏳') +
            ' <span style="color:#94a3b8">— ' + esc(p.desc) + '</span></li>' : ''
        }).join('') + '</ul></div>'
    } else if (n.type === 'stage') {
      const mods = data.modules.filter(function (m) { return m.stage === n.code })
      html += '<span class="badge" style="background:' + colorOf(n.code) + '">阶段</span>' +
        '<h2>' + esc(n.name) + '</h2>' +
        '<div class="meta">' + (n.progress != null ? '学习进度 ' + n.progress + '%' : '—') + '</div>' +
        '<div class="block"><h3>包含模块</h3><ul>' +
        mods.map(function (m) { return '<li>' + moduleLink(m) + '</li>' }).join('') + '</ul></div>'
    } else if (n.id === 's:future') {
      html += '<span class="badge" style="background:#94a3b8">规划</span>' +
        '<h2>' + esc(n.name) + '</h2>' +
        '<div class="meta">尚未开始的学习方向</div>' +
        '<div class="block"><h3>规划条目</h3><ul>' +
        data.planned.filter(function (p) { return p.stage === null })
          .map(function (p) { return '<li>' + esc(p.name) + '</li>' }).join('') + '</ul></div>'
    } else {
      html += '<span class="badge" style="background:#94a3b8">规划中</span>' +
        '<h2>' + esc(n.name) + '</h2>' +
        '<div class="meta">学完后更新 KNOWLEDGE_BASE.md 并重跑生成器</div>'
    }
    detailEl.innerHTML = html
    document.getElementById('detail-close').addEventListener('click', function () {
      selected = null
      showPlaceholder()
      render()
    })
    detailEl.querySelectorAll('a[data-point]').forEach(function (a) {
      a.addEventListener('click', function () {
        const t = byId.get(a.getAttribute('data-point'))
        if (t) { t.visible = true; openDetail(t) }
      })
    })
    detailEl.querySelectorAll('a[data-module]').forEach(function (a) {
      a.addEventListener('click', function () {
        const m = byId.get(a.getAttribute('data-module'))
        if (m) { m.visible = true; openDetail(m) }
      })
    })
    render()
  }

  // ---------- 侧边栏 ----------
  function renderStats() {
    const s = data.stats
    let learned = 0
    for (const p of data.points) if (p.learned) learned++
    const cells = [
      ['阶段', s.stages], ['模块', s.modules], ['知识点', s.knowledge],
      ['✅ 已学', learned], ['⏳ 未学', s.knowledge - learned], ['直接关联', s.related],
      ['踩坑', s.pitfalls], ['规划中', s.planned], ['学习日', data.days.length],
    ]
    document.getElementById('stats').innerHTML = cells.map(function (x) {
      return '<div class="cell"><b>' + x[1] + '</b><span>' + x[0] + '</span></div>'
    }).join('')
  }

  function renderStageFilters() {
    const box = document.getElementById('stage-filter')
    box.innerHTML = data.stages.map(function (s) {
      return '<label><input type="checkbox" data-key="' + esc(s.code) + '" checked>' +
        '<span class="dot" style="background:' + bgOf(s.code) + '"></span>' + esc(s.name) + '</label>'
    }).join('') +
      (data.planned.some(function (p) { return p.stage === null })
        ? '<label><input type="checkbox" data-key="future" checked>' +
          '<span class="dot" style="background:#94a3b8"></span>🔜 未来规划</label>'
        : '')
    box.querySelectorAll('input').forEach(function (cb) {
      cb.addEventListener('change', function () { applyFilters(); render() })
    })
  }

  function applyFilters() {
    const q = document.getElementById('search').value.trim().toLowerCase()
    const checked = new Set()
    document.querySelectorAll('#stage-filter input:checked').forEach(function (cb) {
      checked.add(cb.getAttribute('data-key'))
    })
    for (const n of nodes) {
      let base = true
      if (n.type === 'stage' || n.type === 'future') base = checked.has(n.code)
      else if (n.type === 'module' || n.type === 'knowledge') base = checked.has(n.stage)
      else if (n.type === 'planned') base = n.stage === null ? checked.has('future') : checked.has(n.stage)
      let match = true
      if (q) {
        let hay = (n.name || '') + ' ' + (n.desc || '') + ' ' + (n.code || '')
        if (n.pitfalls) {
          hay += ' ' + n.pitfalls.map(function (p) { return p.err + ' ' + p.fix }).join(' ')
        }
        match = hay.toLowerCase().indexOf(q) !== -1
      }
      n.visible = base && match
      n.dim = match ? 1 : 0.05
    }
    if (hovered && !hovered.visible) hovered = null
    if (focusModule && !focusModule.visible) focusModule = null
    fitToVisible()
  }

  document.getElementById('search').addEventListener('input', function () { applyFilters(); render() })
  document.getElementById('btn-all').addEventListener('click', function () {
    document.querySelectorAll('#stage-filter input').forEach(function (cb) { cb.checked = true })
    applyFilters(); render()
  })
  document.getElementById('btn-none').addEventListener('click', function () {
    document.querySelectorAll('#stage-filter input').forEach(function (cb) { cb.checked = false })
    applyFilters(); render()
  })
  document.getElementById('btn-fit').addEventListener('click', fitView)
  document.getElementById('btn-relayout').addEventListener('click', fitView)

  // ---------- 启动 ----------
  renderStats()
  renderStageFilters()
  showPlaceholder()
  computeLayout()
  applyFilters()
  resize()
  window.addEventListener('resize', function () { resize(); render() })
  // Inter 字体加载完成后，重新量字布局并重绘（画布不会自动响应字体加载）
  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(function () {
      computeLayout()
      applyFilters()
    })
  }
  render()
})()
