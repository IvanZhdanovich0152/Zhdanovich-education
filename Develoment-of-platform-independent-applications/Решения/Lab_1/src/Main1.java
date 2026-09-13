import java.util.Scanner;

public class Main1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.print("Введите дистанцию поездки >>> ");
            int distanceKm = scanner.nextInt();

            System.out.print("Введите тип вагона ('S' — сидячий, 'C' — купе,\n" +
                    "'L' — люкс) >>> ");
            char carriageType = scanner.next().charAt(0);

            System.out.print("Введите ваш возраст >>> ");
            int age = scanner.nextInt();

            System.out.print("Наличие багажа (y/n) >>> ");
            boolean hasBaggage = scanner.next().equals("y");

            if (distanceKm > 1000 && carriageType == 'C') {
                System.out.println("Питание включено");
            }

            double basePrice = switch (Character.toLowerCase(carriageType)) {
                case 's' -> 5.0;
                case 'c' -> 10.0;
                case 'l' -> 20.0;
                default -> throw new IllegalArgumentException();
            };

            double cost = basePrice * distanceKm;

            if (age < 10) {
                cost *= 0.5;
            }

            if (age >= 18 && age <= 25 && (carriageType == 'S' || carriageType == 'C')) {
                cost *= 0.75;
            }

            if (hasBaggage && carriageType != 'L') {
                cost += 200.0;
            }

            if (distanceKm > 500) {
                cost *= 0.9;
            }

            System.out.printf("Стоимость билета: %.2f руб.", cost);

        } catch (Exception e) {
            System.err.println("Ошибка ввода: Пожалуйста, введите данные согласно региональным настройкам.");
        } finally {
            scanner.close();
        }
    }
}