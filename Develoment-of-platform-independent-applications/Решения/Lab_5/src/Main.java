import java.util.Scanner;

class Main {
    static void main() {
        Scanner scanner = new Scanner(System.in);
        WateringSystemUI UI = new WateringSystemUI(scanner);
        UI.start();
        scanner.close();
    }
}
