package greenbrier.drinkmixer3000;

/**
 * Created by McGiv on 8/30/2017.
 */

public class Drink implements Comparable<Drink>
{
    public final String name;
    public final boolean alcoholic;


    public Drink(String name, boolean alc)
    {
        this.name = name;
        this.alcoholic = alc;
    }

    @Override
    public boolean equals(Object d)
    {
        return name.equals(((Drink)d).name) && alcoholic == ((Drink)d).alcoholic;
    }

    public int compareTo(Drink d)
    {
        return name.compareTo(d.name);
    }



}
