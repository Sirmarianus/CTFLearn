import java.util.HashMap;
import java.util.Map;

public class Main{

    public static void main(String [] args){
        Map<Integer, Integer> map = new HashMap<>();

        map.put(20, 100);
        map.put(0, 67);
        map.put(24, 125);
        map.put(19, 51);
        map.put(5, 97);
        map.put(11, 117);
        map.put(9, 121);
        map.put(8, 123);
        map.put(16, 116);
        map.put(4, 101);
        map.put(13, 99);
        map.put(21, 95);
        map.put(2, 70);
        map.put(3, 108);
        map.put(23, 51);
        map.put(15, 112);
        map.put(10, 48);
        map.put(17, 117);
        map.put(6, 114);
        map.put(1, 84);
        map.put(14, 52);
        map.put(7, 110);
        map.put(18, 114);
        map.put(22, 109);
        map.put(12, 95);

        for (int i=0; i<25; i++){
            System.out.print(Character.toChars(map.get(i)));
        }
    }

}