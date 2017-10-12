package com.a.k.drinkmixer;

import android.os.Parcel;
import android.os.Parcelable;

import java.util.ArrayList;

/**
 * Created by McGiv on 9/9/2017.
 */

public class DrinksParcelable implements Parcelable
{
    public final ArrayList<Drink> drinks;
    public final ArrayList<Mix> mixes;

    public DrinksParcelable(ArrayList<Drink> d, ArrayList<Mix> m)
    {
        drinks = new ArrayList<Drink>();
        mixes = new ArrayList<Mix>();

        drinks.addAll(d);
        mixes.addAll(m);
    }


    public static final Creator<DrinksParcelable> CREATOR = new Creator<DrinksParcelable>()
    {
        @Override
        public DrinksParcelable createFromParcel(Parcel in) {
            return new DrinksParcelable(in);
        }

        @Override
        public DrinksParcelable[] newArray(int size) {
            return new DrinksParcelable[size];
        }
    };


    public DrinksParcelable(Parcel in)
    {
        drinks = new ArrayList<Drink>();
        mixes = new ArrayList<Mix>();

        int drinkCount = in.readInt();
        for(int x =0; x< drinkCount; x++)
        {
            drinks.add((Drink)in.readParcelable(Drink.class.getClassLoader()));
        }
        drinkCount = in.readInt();//actually mixes now
        for(int x = 0; x< drinkCount; x++)
        {
            mixes.add((Mix)in.readParcelable(Mix.class.getClassLoader()));
        }
    }

    @Override
    public void writeToParcel(Parcel dest, int flags)
    {
        dest.writeInt(drinks.size());
        for(Drink d : drinks)
            dest.writeParcelable(d, 0);
        dest.writeInt(mixes.size());
        for(Mix m : mixes)
            dest.writeParcelable(m, 0);
    }

    @Override
    public int describeContents()
    {
        return 0;
    }
}
