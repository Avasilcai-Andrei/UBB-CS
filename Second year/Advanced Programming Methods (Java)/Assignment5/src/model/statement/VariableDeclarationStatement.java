package model.statement;

import exceptions.StatementExecutionException;
import model.state.ProgramState;
import model.type.Type;

public record VariableDeclarationStatement(Type type, String variableName) implements Statement {

    @Override
    public ProgramState execute(ProgramState state) {
        var symbolTable = state.symbolTable();
        if (symbolTable.isDefined(variableName)) {
            throw new StatementExecutionException("Variable '" + variableName + "' is already defined");
        }
        symbolTable.declareVariable(variableName, type);
        return null;
    }

    @Override
    public String toString() {
        return type + " " + variableName;
    }
}
