package model.statement;

import exceptions.StatementExecutionException;
import model.expression.Expression;
import model.state.ProgramState;
import model.state.SymbolTable;
import model.value.Value;

public record AssignmentStatement(Expression expression, String variableName) implements Statement {

    @Override
    public ProgramState execute(ProgramState state) {
        SymbolTable symbolTable = state.symbolTable();
        if (!symbolTable.isDefined(variableName)) {
            throw new StatementExecutionException("Variable '" + variableName + "' is not defined");
        }
        Value value = expression.evaluate(symbolTable, state.heap());
        if (!value.getType().equals(symbolTable.getType(variableName))) {
            throw new StatementExecutionException("Type mismatch for variable '" + variableName + "'");
        }
        symbolTable.update(variableName, value);
        return null;
    }

    @Override
    public String toString() {
        return variableName + " = " + expression;
    }
}
