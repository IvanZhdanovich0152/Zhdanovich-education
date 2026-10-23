import java.util.Scanner;

// Реализовать такой же фабричный метод, что и в 5 лабе

public class Main {
    public static void main(String[] args) {
        new ComputerUI(new Scanner(System.in)).start();
    }
}
