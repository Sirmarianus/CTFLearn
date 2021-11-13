import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashMap;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Scanner;


public class Main {

    public static void main(String [] args) throws FileNotFoundException{
        String file = "C:\\Users\\Legio\\Desktop\\CTF\\~Unfinished\\Q's Cubes\\in";
        Scanner scanner = new Scanner(new File(file));

        Map<Point, Character> map = new HashMap<>();
        Queue<Point> queue = new LinkedList<>();

        int x = 0;
        int y = 0;
        while(scanner.hasNext()){
            String s = scanner.nextLine();
            for (char c : s.toCharArray()){
                Point p = new Point(x, y, 0);
                queue.add(p);
                map.put(p, c);
                x += 1;
            }
            x = 0;
            y += 1;
        }

        // dimensions
        x = y;
        int z = 1;
        int numberOfPoints = y*y;

        for (int i=0; i<4; i++){
            for (int j=0; j<numberOfPoints; j++){
                Point p = queue.poll();
                if (p.y < y/2){
                    p.z = z*2-1-p.z;
                    p.y = y-1-p.y;
                }
                p.y -= y/2;
                queue.add(p);
            }
            y = y/2;
            z = z*2;

            for (int j=0; j<numberOfPoints; j++){
                Point p = queue.poll();
                if (p.x < x/2){
                    p.z = z*2-1-p.z;
                    p.x = x-1-p.x;
                }
                p.x -= x/2;
                queue.add(p);
            }
            x = x/2;
            z = z*2;
        }
        StringBuilder sb = new StringBuilder();
        sb.append("a".repeat(numberOfPoints));

        for (int j=0; j<numberOfPoints; j++){
            Point p = queue.poll();
            sb.setCharAt(p.z, map.get(p));
        }
        System.out.println(sb.reverse());
    }
}
