import java.util.Scanner;

class Main {
    static void main() {
        Scanner sc = new Scanner(System.in);

        int n;
        do {
            System.out.print("Введите размер массива >>> ");
            n = sc.nextInt();
            if (n == 0) {
                System.out.println("Кол-во элементов не должно ровняться 0.\n");
            }
        } while (n == 0);


        double[] sizes = new double[n];
        boolean has_negative = false;
        do {
            System.out.printf("Введите размеры деталей (%d шт), через пробел, только положительные >>> ", n);
            for (int i = 0; i < n; i++) {
                sizes[i] = sc.nextDouble();
                if (sizes[i] < 0) {
                    has_negative = true;
                }
            }
        } while (has_negative);


        double idealSize;
        do {
            System.out.print("Введите идеальный размер детали >>> ");
            idealSize = sc.nextDouble();
            if (idealSize < 0) {
                System.out.println("Идеальный размер не может быть отрицательным.\n");
            }
        } while (idealSize < 0);


        int countDefectDetails = countDefectiveDetails(sizes, idealSize);

        System.out.print("Размеры деталей с конвейера:  ");
            for (double j : sizes) {
                System.out.print(j + " ");
            }
        System.out.printf("%nВсего бракованных деталей обнаружено: %d", countDefectDetails);

        sc.close();
    }

    static double calculateDeviation(double size, double idealSize){
        return Math.abs(idealSize - size);
    }

    static boolean isDefective(double deviation) {
        return deviation > 0.5;
    }

    static int countDefectiveDetails(double[] sizes, double idealSize) {
        int count = 0;
        for (double size : sizes) {
            if (isDefective(calculateDeviation(size, idealSize))) {
                count++;
            }
        }
        return count;
    }
}