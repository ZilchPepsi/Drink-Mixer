package com.a.k.drinkmixer;

import android.os.Parcel;
import android.os.Parcelable;

import java.util.ArrayList;
import java.util.TreeMap;

/**
 * Created by McGiv on 8/30/2017.
 */

public class Mix implements Parcelable
{
    private String name;
    private TreeMap<Drink, Integer> drinks;

    public Mix(String name)
    {
        this.name = name;
        drinks = new TreeMap<Drink, Integer>();
    }

    protected Mix(Parcel in)
    {

        name = in.readString();
        drinks = new TreeMap<Drink, Integer>();
        int drinkCount = in.readInt();
        for(int x =0; x< drinkCount; x++)
        {
            drinks.put((Drink)in.readParcelable(Drink.class.getClassLoader()), in.readInt());
        }
    }

    public static final Creator<Mix> CREATOR = new Creator<Mix>() {
        @Override
        public Mix createFromParcel(Parcel in) {
            return new Mix(in);
        }

        @Override
        public Mix[] newArray(int size) {
            return new Mix[size];
        }
    };

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


    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel parcel, int i)
    {
        parcel.writeString(name);
        parcel.writeInt(drinks.size());

        for(Drink d : drinks.keySet())
        {
            parcel.writeParcelable(d,0);
            parcel.writeInt(drinks.get(d));
        }
    }
}
