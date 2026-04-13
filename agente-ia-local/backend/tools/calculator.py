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
    if isinstance(node, ast.Num):
        return node.n
    elif isinstance(node, ast.BinOp):
        op = ALLOWED_OPS.get(type(node.op))
        if op is None:
            raise ValueError("Operação não permitida")
        return op(safe_eval(node.left), safe_eval(node.right))
    elif isinstance(node, ast.UnaryOp):
        op = ALLOWED_OPS.get(type(node.op))
        return op(safe_eval(node.operand))
    else:
        raise ValueError(f"Expressão não suportada: {type(node)}")

def calculator(expression: str) -> str:
    try:
        tree = ast.parse(expression, mode='eval')
        result = safe_eval(tree.body)
        return f"Resultado: {result}"
    except Exception as e:
        return f"Erro no cálculo: {str(e)}"