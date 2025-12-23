import random

if __name__ == "__main__":
    num = 2000
    operators = ['+','-','x']
    file = "math.txt"

    with open(file, 'w', encoding='utf-8') as f:
        for n in range(num):
            oper = random.choice(operators)
            match oper:
                case '+':
                    i = random.randint(0,99)
                    j = random.randint(0,100-i)
                case '-':
                    i = random.randint(1,99)
                    j = random.randint(0,i)
                case 'x':
                    i = random.randint(0,9)
                    j = random.randint(0,9)

            q = "{0:3}  {1}  {2:2} = \n".format(i,oper,j)

            f.write(q)
    print("已生成{}道题目".format(num))
