import java.util.Scanner;

public class Main {
    static void main() {
        Scanner scanner = new Scanner(System.in);

        int prev = 0;
        int now;
        int mainShockCount = 0;
        int afterShockCount = 0;
        int afterShockStreak = 0;
        boolean wasMainShock = false;
        boolean hasAfterShockSeries = false;

        do {
            System.out.print("Введите магнитуду. 0 - завершение. >>> ");
            now = scanner.nextInt();

            if (now >= 50) {
                mainShockCount++;
                wasMainShock = true;
                afterShockStreak = 0;
            }

            if (wasMainShock && now >= 30 && now < prev) {
                afterShockCount++;
                afterShockStreak++;

                if (afterShockStreak >= 3) {
                    hasAfterShockSeries = true;
                }
            } else {
                if (now <= 30 || now >= prev) {
                    afterShockStreak = 0;
                }
            }

            prev = now;

        } while (now != 0);

        System.out.printf("Основных толчков: %d, Афтершоков: %d, Серия афтершоков: %s%n",
                mainShockCount,
                afterShockCount,
                hasAfterShockSeries ? "да" : "нет");

        scanner.close();
    }
}

