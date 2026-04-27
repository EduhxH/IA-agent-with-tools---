import ast
import operator

ALLOWED_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
}


def safe_eval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    elif isinstance(node, ast.BinOp):
        op = ALLOWED_OPS.get(type(node.op))
        if op is None:
            raise ValueError("Operation not allowed")
        return op(safe_eval(node.left), safe_eval(node.right))
    elif isinstance(node, ast.UnaryOp):
        op = ALLOWED_OPS.get(type(node.op))
        return op(safe_eval(node.operand))
    else:
        raise ValueError(f"Unsupported expression: {type(node)}")


def calculator(expression: str) -> str:
    try:
        tree = ast.parse(expression, mode="eval")
        result = safe_eval(tree.body)
        return f"Result: {result}"
    except Exception as e:
        return f"Calculation error: {str(e)}"