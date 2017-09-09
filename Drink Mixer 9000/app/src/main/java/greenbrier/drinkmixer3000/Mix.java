package greenbrier.drinkmixer3000;

import java.util.ArrayList;
import java.util.TreeMap;

/**
 * Created by McGiv on 8/30/2017.
 */

public class Mix
{
    private String name;
    private TreeMap<Drink, Integer> drinks;

    public Mix(String name)
    {
        this.name = name;
        drinks = new TreeMap<Drink, Integer>();
    }

    public void addDrink(Drink d, int shots)
    {
        drinks.put(d,shots);
    }

    public String getName()
    {
        return name;
    }
    public TreeMap<Drink,Integer> getDrinks()
    {
        return drinks;
    }

    @Override
    public boolean equals(Object m)
    {
        return name.equals(((Mix)m).name);
    }


}
