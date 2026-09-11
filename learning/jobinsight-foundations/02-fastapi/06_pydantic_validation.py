from pydantic import BaseModel, Field, ValidationError

class Candidate(BaseModel):
    name: str = Field(min_length=1)
    age: int = Field(ge=16, le=100)
    skills: list[str] = Field(min_length=1)

def main():
    # 1. 正确类型
    person = Candidate(name="小明", age=20,skills=["Python"])
    print("正常输入：", person.model_dump())

    # 2. 可以转换，但不满足范围
    try:
        person = Candidate(name="小红", age="15",skills=["Python"])
        print("转换后的年龄：", person.age)
        print("转换后的类型：", type(person.age).__name__)
    except ValidationError as error:
        print("年龄范围校验失败：")
        print(error)

    # 3. 无法转换的字符串
    try:
        person = Candidate(name="小刚", age="abc",skills=["Python"])
        print("创建成功")
    except ValidationError as error:
        print("校验失败：")
        print(error)

    try:
        person = Candidate(name="小王", age=20, skills=[])
        print("创建成功")
    except ValidationError as error:
        print("技能校验失败：")
        print(error)    

    print("\n全部测试结束")

if __name__ == "__main__":
    main()
