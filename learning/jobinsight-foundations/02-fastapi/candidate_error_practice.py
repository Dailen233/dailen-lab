from unittest.mock import MagicMock, patch

from fastapi import HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from candidate_app.routers.candidates import create_candidate
from candidate_app.schemas import CandidateInput


def check_error_case(stage, expected_detail):
    fake_session = MagicMock(spec=Session)

    if stage == "commit":
        fake_session.commit.side_effect = SQLAlchemyError("模拟提交异常")
    else:
        fake_session.refresh.side_effect = SQLAlchemyError("模拟读取异常")

    data = CandidateInput(
        name="模拟候选人",
        target_job="Python 后端开发"
    )

    # 暂时替换日志记录器，让测试输出更容易阅读
    with patch("candidate_app.routers.candidates.logger"):
        try:
            create_candidate(data=data, session=fake_session)

        except HTTPException as error:
            assert error.status_code == 500
            assert error.detail == expected_detail

        else:
            raise AssertionError("预期抛出 HTTPException，但没有发生")

    fake_session.commit.assert_called_once_with()
    fake_session.rollback.assert_called_once_with()

    if stage == "commit":
        fake_session.refresh.assert_not_called()
    else:
        fake_session.refresh.assert_called_once()

    print(stage + " 异常分支：通过")


if __name__ == "__main__":
    check_error_case(
        "commit",
        "候选人保存异常，请先查询列表确认结果。"
    )

    check_error_case(
        "refresh",
        "候选人已保存，但读取结果失败，请刷新列表确认。"
    )
    