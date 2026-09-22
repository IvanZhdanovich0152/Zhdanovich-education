class Main {
    public static void main(String[] args) {

//        int[] arr = {1, 4, 7, 2, 10, 13, 5, 8, 11, 14};
        int[] arr = {2, 1, 4, 5, 7, 10, 8, 11, 13, 14};
//        int[] arr = {1, 2, 4, 7, 5, 8, 10, 13, 11, 14};
//        int[] arr = {1, 4, 7, 10, 2, 5, 8, 11};
//        int[] arr = {1, 2, 4, 5, 7, 8};

        // A = {1,4,7,10,13,16}
        // B = {2,5,8,11,14,17}


        System.out.print("Исходный массив: ");
        for (int value : arr) {
            System.out.print(value + " ");
        }

        int n = arr.length;
        int i = 0;
        int j = 0;
        int lastA = 0;
        int lastB = 0;

        while (i < n && j < n) {
            if (arr[i] % 3 != 1 || arr[i] <= lastA) {
                i++;
                continue;
            }

            if (arr[j] % 3 != 2 || arr[j] <= lastB) {
                j++;
                continue;
            }

            lastA = arr[i];
            lastB = arr[j];

            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;

            i++;
            j++;
        }

        System.out.print("\nМассив после перестановки: ");
        for (int new_value : arr) {
            System.out.print(new_value + " ");
        }
    }
}