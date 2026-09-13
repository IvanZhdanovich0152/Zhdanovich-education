import java.util.Scanner;

public class Main2 {
    public static void main() {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Функция задана тремя ветками:");
        System.out.println("  1) y = ln(ln(x)),          если x < a");
        System.out.println("  2) y = sqrt(x^2 - b^2),    если a <= x <= b^2");
        System.out.println("  3) y = e^(ax) + sin(z),    если x > b^2");
        System.out.println();
        System.out.println("Ограничения:");
        System.out.println("  - Для ветки 1: x > 1");
        System.out.println("  - Для ветки 2: |x| >= |b|");
        System.out.println("  - Для ветки 3: ограничений нет");

        System.out.println("Введите значение x >>> ");
        double x = scanner.nextDouble();

        System.out.print("Введите значение a >>> ");
        double a = scanner.nextDouble();

        System.out.print("Введите значение b >>> ");
        double b = scanner.nextDouble();

        System.out.print("Введите значение z >>> ");
        double z = scanner.nextDouble();

        System.out.println();
        System.out.println("Входные данные:");
        System.out.printf("x = %.4f, a = %.4f, b = %.4f, z = %.4f%n", x, a, b, z);
        System.out.printf("b^2 = %.4f%n", b * b);

        try {
            double result = calculateFunction(x, a, b, z);
            System.out.println();
            System.out.printf("Результат: y(%.4f) = %.6f%n", x, result);
        } catch (IllegalArgumentException e) {
            System.err.println();
            System.err.println(e.getMessage());
        }

        scanner.close();
    }

    public static double calculateFunction(double x, double a, double b, double z) {
        double bSquared = b * b;

        if (x < a) {
            if (x <= 0) {
                throw new IllegalArgumentException(
                        "ОШИБКА: Для первой ветки (x < a) требуется x > 0, " +
                                "так как используется ln(ln(x)). Текущее x = " + x
                );
            }
            if (Math.log(x) <= 0) {
                throw new IllegalArgumentException(
                        "ОШИБКА: Для первой ветки (x < a) требуется ln(x) > 0, " +
                                "так как используется ln(ln(x)). Текущее ln(" + x + ") = " + Math.log(x)
                );
            }
            return Math.log(Math.log(x));
        }

        if (x >= a && x <= bSquared) {
            double expression = x * x - bSquared;
            if (expression < 0) {
                throw new IllegalArgumentException(
                        "ОШИБКА: Для второй ветки (a <= x <= b^2) требуется x^2 - b^2 >= 0. " +
                                "Текущее значение: " + x + "^2 - " + b + "^2 = " + expression
                );
            }
            return Math.sqrt(expression);
        }

        if (x > bSquared) {
            return Math.exp(a * x) + Math.sin(z);
        }
        throw new IllegalArgumentException(
                "ОШИБКА: Значение x не попадает ни в одну из областей определения."
        );
    }
}