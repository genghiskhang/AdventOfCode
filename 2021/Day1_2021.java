import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.ArrayList;

class Day1_2021 {
    static ArrayList<Integer> dataset = new ArrayList<>();
    static {
        try {
            File txt = new File("2021day1input.txt");
            Scanner read = new Scanner(txt);
            while (read.hasNextLine()) {
                dataset.add(Integer.parseInt(read.nextLine()));
            }
            read.close();
        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args) {
        System.out.println(part1(dataset));
        System.out.println(part2(dataset));
    }

    public static int part1(ArrayList<Integer> input) {
        int increase = 0;
        for (int i = 1; i < input.size(); i++) {
            if (input.get(i) > input.get(i - 1)) {
                increase++;
            }
        }
        return increase;
    }

    public static int part2(ArrayList<Integer> input) {
        int increase = 0;
        for (int i = 3; i < input.size(); i++) {
            if (input.get(i) + input.get(i - 1) + input.get(i - 2) > input.get(i - 1) + input.get(i - 2) + input.get(i - 3)) {
                increase++;
            }
        }
        return increase;
    }
}