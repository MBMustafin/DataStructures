from algoritms.data_structures.stack_linked_list import StackLinkedList


def is_valid_parentheses(s:str) -> bool:
    stack = StackLinkedList()                         #()(){{[()]}}
    br_dict = { ")" : "(", "}": "{", "]": "[", ">": "<"}
    for i in range(len(s)):
        if s[i] in "[{(<":
            stack.push(s[i])
        elif s[i] in "]})>":
            if stack.is_empty():
                return False
                # Только потом pop()
            if br_dict[s[i]] != stack.pop():
                return False


    return stack.is_empty()




s = "()(){{[(]}}"
print(is_valid_parentheses(s))