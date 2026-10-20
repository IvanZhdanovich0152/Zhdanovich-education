//TIP Вариант 6

void main() {
    IO.println("Hello and welcome!");

    Computer computer = new Computer();
    computer.turnOn();

    IO.println(computer.isPowerOn());
    computer.turnoff();

    IO.println(computer.checkSystemStatus());

    IO.println(computer.showSystemInfo());
}

