package model.state;

import model.statement.Statement;

public class ProgramState {
    private final ExecutionStack executionStack;
    private final SymbolTable symbolTable;
    private final Out out;
    private final FileTable fileTable;
    private final Statement originalProgram;

    public ProgramState(ExecutionStack executionStack,
                        SymbolTable symbolTable,
                        Out out,
                        FileTable fileTable,
                        Statement originalProgram) {
        this.executionStack = executionStack;
        this.symbolTable = symbolTable;
        this.out = out;
        this.fileTable = fileTable;
        this.originalProgram = originalProgram;

        this.executionStack.push(originalProgram);
    }

    public ExecutionStack executionStack() {
        return executionStack;
    }

    public SymbolTable symbolTable() {
        return symbolTable;
    }

    public Out out() {
        return out;
    }

    public FileTable fileTable() {
        return fileTable;
    }

    public Statement originalProgram() {
        return originalProgram;
    }

    public boolean isCompleted() {
        return executionStack.isEmpty();
    }

    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();
        sb.append("\n=== Program State ===\n");

        sb.append("Execution Stack:\n");
        sb.append(executionStack.toString()).append("\n");

        sb.append("Symbol Table:\n");
        sb.append(symbolTable.toString()).append("\n");

        sb.append("Output:\n");
        sb.append(out.toString()).append("\n");

        sb.append("File Table:\n");
        sb.append(fileTable.toString()).append("\n");

        sb.append("======================\n");
        return sb.toString();
    }
}
