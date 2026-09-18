import java.util.Scanner;

public class Main2 {
    public static void main() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите значение x >>> ");
        double x = scanner.nextDouble();

        System.out.print("Введите значение a >>> ");
        double a = scanner.nextDouble();

        System.out.print("Введите значение b >>> ");
        double b = scanner.nextDouble();

        System.out.print("Введите значение z >>> ");
        double z = scanner.nextDouble();

        System.out.println();

        String errorMessage = "";
        double result;
        double bSquared = b * b;

        if (x < a) {
            if (x <= 1) {
                errorMessage = "ОШИБКА: Для первой ветки (x < a) требуется x > 1, так как используется ln(ln(x)). Текущее x = " + x;
            }
            result = Math.log(Math.log(x));

        } else if (x <= bSquared) {
            double expression = x * x - bSquared;
            if (expression < 0) {
                errorMessage = "ОШИБКА: Для второй ветки (a <= x <= b^2) требуется x^2 - b^2 >= 0.";
            }

            result = Math.sqrt(expression);

        } else {
            result = Math.exp(a * x) + Math.sin(z);
        }

        if (!errorMessage.isEmpty()){
            System.out.print(errorMessage);

        }else {
            System.out.printf("Результат: y(%.4f) = %.6f%n", x, result);
        }

        scanner.close();
    }
}

