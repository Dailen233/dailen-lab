from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from candidate_app.models import Candidate


def get_names(session):
    statement = select(Candidate.name).order_by(Candidate.id)
    return session.scalars(statement).all()


def main():
    # 创建独立的内存数据库
    practice_engine = create_engine("sqlite:///:memory:")

    # 在这个内存数据库里创建候选人表
    Candidate.__table__.create(practice_engine)

    # 实验一：成功提交
    with Session(practice_engine) as session:
        session.add(
            Candidate(name="小明", target_job="Python 后端开发")
        )
        session.add(
            Candidate(name="小红", target_job="Vue 前端开发")
        )

        session.commit()
        print("实验一：已提交小明和小红")

    # 实验二：写入后发生异常，执行回滚
    with Session(practice_engine) as session:
        try:
            session.add(
                Candidate(name="回滚测试甲", target_job="AI 应用开发")
            )
            session.add(
                Candidate(name="回滚测试乙", target_job="Java 后端开发")
            )

            session.flush()
            print("回滚前，当前事务看到：", get_names(session))

            simulate_failure = True

            if simulate_failure:
                raise ValueError("模拟后续业务步骤失败")

            session.commit()

        except ValueError as error:
            session.rollback()
            print("已回滚：", error)

    # 实验三：用新会话检查最终结果
    with Session(practice_engine) as session:
        print("新会话查询结果：", get_names(session))

    practice_engine.dispose()


if __name__ == "__main__":
    main()