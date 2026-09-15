import sqlite3
from pathlib import Path


DB_PATH = Path(__file__).resolve().parent / "candidates_learning.db"


def main():
    connection = sqlite3.connect(DB_PATH)

    try:
        # 1. 创建表
        connection.execute("""
            CREATE TABLE IF NOT EXISTS candidates (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                target_job TEXT NOT NULL
            )
        """)

        # 2. 准备候选人数据
        candidates = [
            (1, "小明", "Python 后端开发"),
            (2, "小红", "前端开发"),
            (3, "小刚", "FastAPI 后端开发")
        ]

        # 3. 批量插入，已有相同 ID 时跳过
        connection.executemany("""
            INSERT INTO candidates (id, name, target_job)
            VALUES (?, ?, ?)
            ON CONFLICT(id) DO NOTHING
        """, candidates)

        # 4. 提交修改
        connection.commit()

        # 5. 查询所有候选人
        cursor = connection.execute("""
            SELECT id, name, target_job
            FROM candidates
            ORDER BY id
        """)

        for row in cursor.fetchall():
            print(row)

        print("数据库位置：", DB_PATH)

        cursor = connection.execute(
            """
            SELECT id, name
            FROM candidates
            WHERE target_job LIKE ?
            """,
            ("%后端%",)
        )

        for row in cursor.fetchall():
            print(row)

        cursor = connection.execute(
            """
            UPDATE candidates
            SET target_job = ?
            WHERE id = ?
            """,
            ("Vue 前端开发", 2)
        )

        connection.commit()

        cursor = connection.execute(
            "SELECT id, name, target_job FROM candidates WHERE id = ?",
            (2,)
        )

        print(cursor.fetchone())

        cursor = connection.execute(
            "SELECT id, name FROM candidates WHERE id = ?",
            (99,)
        )
        print("fetchone 未找到：", cursor.fetchone())

        cursor = connection.execute(
            "SELECT id, name FROM candidates WHERE id = ?",
            (99,)
        )
        print("fetchall 未找到：", cursor.fetchall())

        # 6. 删除候选人，但暂不提交
        cursor = connection.execute(
            "DELETE FROM candidates WHERE id = ?",
            (3,)
        )
        print("本次删除行数：", cursor.rowcount)

        # 当前连接可以看到尚未提交的删除结果
        row = connection.execute(
            "SELECT id, name FROM candidates WHERE id = ?",
            (3,)
        ).fetchone()
        print("删除后、回滚前：", row)

        # 7. 撤销本次未提交的删除
        connection.rollback()

        row = connection.execute(
            "SELECT id, name FROM candidates WHERE id = ?",
            (3,)
        ).fetchone()
        print("回滚后：", row)
        
    finally:
        connection.close()


if __name__ == "__main__":
    main()