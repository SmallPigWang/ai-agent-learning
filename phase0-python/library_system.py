# ============================================================
# 练习: 图书馆管理系统（面向对象基础）
#
# 实现两个类:
#
#   Book — 一本书
#     __init__(self, title: str, author: str, isbn: str)
#       属性: title 书名, author 作者, isbn ISBN号, available 是否可借(默认True)
#     __repr__(self) → 返回 "《title》- author (isbn)"
#
#   Library — 图书馆
#     __init__(self, name: str)
#       属性: name 馆名, books 书籍列表(初始为空)
#     add_book(self, book: Book) → 无返回值
#       添加一本书。如果 ISBN 已存在则不添加（ISBN 唯一）
#     remove_book(self, isbn: str) → 返回被删除的 Book，没找到返回 None
#     search_by_title(self, keyword: str) → 返回书名包含 keyword 的 Book 列表（大小写不敏感）
#     borrow_book(self, isbn: str) → 返回 True 借阅成功 / False 失败（不存在或已被借走）
#     return_book(self, isbn: str) → 返回 True 归还成功 / False 失败（不存在或未被借出）
#     get_stats(self) → 返回 {"馆名": str, "总藏书": int, "可借": int, "已借出": int}
# ============================================================

class Book:
    """一本书"""
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True

    # 返回对象的字符表示
    def __repr__(self):
        return f"《{self.title}》- {self.author} ({self.isbn})"


class Library:
    """一个图书馆"""
    def __init__(self, name: str):
        self.name = name
        self.books = []

    # 添加一本书
    def add_book(self, book: Book):
        for b in self.books:
            if b.isbn == book.isbn:
                return 
        self.books.append(book)

    # 移除指定的书
    def remove_book(self, isbn: str):
        for i, b in enumerate(self.books):
            if b.isbn == isbn:
                return self.books.pop(i) # 栈顶弹出
        return None

    # 按照关键词找书
    def search_by_title(self, keyword: str):
        result = []
        for b in self.books:
            if keyword.lower() in b.title.lower():
                result.append(b)
        return result

    # 借书
    def borrow_book(self, isbn: str):
        for b in self.books:
            if b.isbn == isbn:
                if b.available:
                    b.available = False
                    return True
                return False
            
        return False

    # 还书
    def return_book(self, isbn: str):
        for b in self.books:
            if b.isbn == isbn:
                if not b.available:
                    b.available = True
                    return True
                return False

        return False

    # 图书馆状态查询
    def get_stats(self):
        avail = 0
        for b in self.books:
            if b.available == True:
                avail += 1

        return {"馆名": self.name, 
                "总藏书": len(self.books), 
                "可借": avail, 
                "已借出": len(self.books) - avail
        }



# ============================================================
# 测试用例
# ============================================================
if __name__ == "__main__":
    # 初始化
    lib = Library("阳光图书馆")

    # 创建书籍
    b1 = Book("三体", "刘慈欣", "978-7-5364-0001-0")
    b2 = Book("活着", "余华", "978-7-5302-0002-7")
    b3 = Book("三体：黑暗森林", "刘慈欣", "978-7-5364-0003-4")
    b4 = Book("百年孤独", "加西亚·马尔克斯", "978-7-5442-0004-1")

    all_pass = True

    # 测试1: 添加书籍
    lib.add_book(b1)
    lib.add_book(b2)
    lib.add_book(b3)
    lib.add_book(b4)
    stats = lib.get_stats()
    if stats == {"馆名": "阳光图书馆", "总藏书": 4, "可借": 4, "已借出": 0}:
        print(f"PASS 添加书籍 -> {stats}")
    else:
        print(f"FAIL 添加书籍 -> {stats} | expected: 总藏书4, 可借4, 已借出0")
        all_pass = False

    # 测试2: ISBN 重复 → 不添加
    lib.add_book(Book("三体 duplicate", "未知", "978-7-5364-0001-0"))
    if lib.get_stats()["总藏书"] == 4:
        print(f"PASS ISBN重复拒绝 -> 总藏书仍为 4")
    else:
        print(f"FAIL ISBN重复拒绝 -> 总藏书 {lib.get_stats()['总藏书']} | expected: 4")
        all_pass = False

    # 测试3: 搜索书名（大小写不敏感）
    results = lib.search_by_title("三体")
    if len(results) == 2 and all(isinstance(b, Book) for b in results):
        print(f"PASS 搜索'三体' -> 找到 {len(results)} 本")
    else:
        print(f"FAIL 搜索'三体' -> {len(results)} 本 | expected: 2")
        all_pass = False

    results = lib.search_by_title("西游记")
    if len(results) == 0:
        print(f"PASS 搜索'西游记'(无结果) -> 找到 0 本")
    else:
        print(f"FAIL 搜索'西游记' -> {len(results)} 本 | expected: 0")
        all_pass = False

    # 测试4: 借阅
    ok = lib.borrow_book("978-7-5364-0001-0")
    if ok == True:
        print(f"PASS 借阅'三体' -> True")
    else:
        print(f"FAIL 借阅'三体' -> {ok} | expected: True")
        all_pass = False

    # 确认已借出
    stats = lib.get_stats()
    if stats["已借出"] == 1 and stats["可借"] == 3:
        print(f"PASS 借阅后统计 -> 可借3, 已借出1")
    else:
        print(f"FAIL 借阅后统计 -> {stats} | expected: 可借3, 已借出1")
        all_pass = False

    # 测试5: 借阅不存在的书
    ok = lib.borrow_book("999-9-9999-9999-9")
    if ok == False:
        print(f"PASS 借阅不存在的书 -> False")
    else:
        print(f"FAIL 借阅不存在的书 -> {ok} | expected: False")
        all_pass = False

    # 测试6: 借阅已借出的书
    ok = lib.borrow_book("978-7-5364-0001-0")
    if ok == False:
        print(f"PASS 重复借阅已借出的书 -> False")
    else:
        print(f"FAIL 重复借阅已借出的书 -> {ok} | expected: False")
        all_pass = False

    # 测试7: 归还
    ok = lib.return_book("978-7-5364-0001-0")
    if ok == True:
        print(f"PASS 归还'三体' -> True")
    else:
        print(f"FAIL 归还'三体' -> {ok} | expected: True")
        all_pass = False

    stats = lib.get_stats()
    if stats["已借出"] == 0 and stats["可借"] == 4:
        print(f"PASS 归还后统计 -> 可借4, 已借出0")
    else:
        print(f"FAIL 归还后统计 -> {stats} | expected: 可借4, 已借出0")
        all_pass = False

    # 测试8: 归还不存在的书
    ok = lib.return_book("999-9-9999-9999-9")
    if ok == False:
        print(f"PASS 归还不存在的书 -> False")
    else:
        print(f"FAIL 归还不存在的书 -> {ok} | expected: False")
        all_pass = False

    # 测试9: 删除书籍
    removed = lib.remove_book("978-7-5302-0002-7")
    if isinstance(removed, Book) and removed.isbn == "978-7-5302-0002-7":
        print(f"PASS 删除'活着' -> {repr(removed)}")
    else:
        print(f"FAIL 删除'活着' -> {removed} | expected: Book对象")
        all_pass = False

    if lib.get_stats()["总藏书"] == 3:
        print(f"PASS 删除后总藏书 -> 3")
    else:
        print(f"FAIL 删除后总藏书 -> {lib.get_stats()['总藏书']} | expected: 3")
        all_pass = False

    # 测试10: __repr__
    if repr(b1) == "《三体》- 刘慈欣 (978-7-5364-0001-0)":
        print(f"PASS __repr__ -> {repr(b1)}")
    else:
        print(f"FAIL __repr__ -> {repr(b1)} | expected: 《三体》- 刘慈欣 (978-7-5364-0001-0)")
        all_pass = False

    # 测试11: 大小写不敏感（新建一个英文书的 Library 独立测试）
    lib2 = Library("英文图书馆")
    lib2.add_book(Book("Clean Code", "Robert Martin", "978-0-1323-5088-4"))
    results = lib2.search_by_title("CLEAN code")  # 混合大小写
    if len(results) == 1:
        print(f"PASS 搜索'CLEAN code'(大小写不敏感) -> 找到 1 本")
    else:
        print(f"FAIL 搜索'CLEAN code' -> {len(results)} 本 | expected: 1")
        all_pass = False

    print(f"\n{'ALL PASS!' if all_pass else 'FAIL - check above'}")
