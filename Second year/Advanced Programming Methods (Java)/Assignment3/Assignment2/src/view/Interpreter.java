package view;

import controller.ControllerImpl;
import model.expression.*;
import model.state.*;
import model.statement.*;
import model.value.BooleanValue;
import model.value.IntegerValue;
import model.value.StringValue;
import repository.RepositoryImpl;
import java.util.Scanner;

public class Interpreter {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter log file base name (e.g. log): ");
        String baseName = scanner.nextLine().trim();
        if (baseName.isEmpty())
            baseName = "log";

        Statement ex1 = new CompoundStatement(
                new VariableDeclarationStatement(model.type.Type.INTEGER, "v"),
                new CompoundStatement(
                        new AssignmentStatement(new ConstantExpression(new IntegerValue(2)), "v"),
                        new PrintStatement(new VariableExpression("v"))
                )
        );
        ProgramState prg1 = new ProgramState(
                new StackExecutionStack(),
                new MapSymbolTable(),
                new ListOut(),
                new MapFileTable(),
                ex1
        );
        RepositoryImpl repo1 = new RepositoryImpl(baseName + "1.txt");
        repo1.addProgram(prg1);
        ControllerImpl ctr1 = new ControllerImpl(repo1);

        Statement ex2 = new CompoundStatement(
                new VariableDeclarationStatement(model.type.Type.INTEGER, "a"),
                new CompoundStatement(
                        new AssignmentStatement(
                                new BinaryOperatorExpression(
                                        "+",
                                        new ConstantExpression(new IntegerValue(2)),
                                        new BinaryOperatorExpression(
                                                "*",
                                                new ConstantExpression(new IntegerValue(3)),
                                                new ConstantExpression(new IntegerValue(5))
                                        )
                                ),
                                "a"
                        ),
                        new CompoundStatement(
                                new VariableDeclarationStatement(model.type.Type.INTEGER, "b"),
                                new CompoundStatement(
                                        new AssignmentStatement(
                                                new BinaryOperatorExpression(
                                                        "+",
                                                        new BinaryOperatorExpression(
                                                                "-",
                                                                new VariableExpression("a"),
                                                                new BinaryOperatorExpression(
                                                                        "/",
                                                                        new ConstantExpression(new IntegerValue(4)),
                                                                        new ConstantExpression(new IntegerValue(2))
                                                                )
                                                        ),
                                                        new ConstantExpression(new IntegerValue(7))
                                                ),
                                                "b"
                                        ),
                                        new PrintStatement(new VariableExpression("b"))
                                )
                        )
                )
        );
        ProgramState prg2 = new ProgramState(
                new StackExecutionStack(),
                new MapSymbolTable(),
                new ListOut(),
                new MapFileTable(),
                ex2
        );
        RepositoryImpl repo2 = new RepositoryImpl(baseName + "2.txt");
        repo2.addProgram(prg2);
        ControllerImpl ctr2 = new ControllerImpl(repo2);

        Statement ex3 = new CompoundStatement(
                new VariableDeclarationStatement(model.type.Type.BOOLEAN, "a"),
                new CompoundStatement(
                        new AssignmentStatement(new ConstantExpression(new BooleanValue(false)), "a"),
                        new CompoundStatement(
                                new VariableDeclarationStatement(model.type.Type.INTEGER, "v"),
                                new CompoundStatement(
                                        new IfStatement(
                                                new VariableExpression("a"),
                                                new AssignmentStatement(new ConstantExpression(new IntegerValue(2)), "v"),
                                                new AssignmentStatement(new ConstantExpression(new IntegerValue(3)), "v")
                                        ),
                                        new PrintStatement(new VariableExpression("v"))
                                )
                        )
                )
        );
        ProgramState prg3 = new ProgramState(
                new StackExecutionStack(),
                new MapSymbolTable(),
                new ListOut(),
                new MapFileTable(),
                ex3
        );
        RepositoryImpl repo3 = new RepositoryImpl(baseName + "3.txt");
        repo3.addProgram(prg3);
        ControllerImpl ctr3 = new ControllerImpl(repo3);

        Statement ex4 = new CompoundStatement(
                new VariableDeclarationStatement(model.type.Type.STRING, "varf"),
                new CompoundStatement(
                        new AssignmentStatement(new ConstantExpression(new StringValue("test.in")), "varf"),
                        new CompoundStatement(
                                new OpenRFileStatement(new VariableExpression("varf")),
                                new CompoundStatement(
                                        new VariableDeclarationStatement(model.type.Type.INTEGER, "varc"),
                                        new CompoundStatement(
                                                new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                                new CompoundStatement(
                                                        new PrintStatement(new VariableExpression("varc")),
                                                        new CompoundStatement(
                                                                new ReadFileStatement(new VariableExpression("varf"), "varc"),
                                                                new CompoundStatement(
                                                                        new PrintStatement(new VariableExpression("varc")),
                                                                        new CloseRFileStatement(new VariableExpression("varf"))
                                                                )
                                                        )
                                                )
                                        )
                                )
                        )
                )
        );
        ProgramState prg4 = new ProgramState(
                new StackExecutionStack(),
                new MapSymbolTable(),
                new ListOut(),
                new MapFileTable(),
                ex4
        );
        RepositoryImpl repo4 = new RepositoryImpl(baseName + "4.txt");
        repo4.addProgram(prg4);
        ControllerImpl ctr4 = new ControllerImpl(repo4);

        TextMenu menu = new TextMenu();
        menu.addCommand(new ExitCommand("0", "Exit the interpreter"));
        menu.addCommand(new RunExample("1", ex1.toString(), ctr1));
        menu.addCommand(new RunExample("2", ex2.toString(), ctr2));
        menu.addCommand(new RunExample("3", ex3.toString(), ctr3));
        menu.addCommand(new RunExample("4", ex4.toString(), ctr4));
        menu.show();
    }
}
