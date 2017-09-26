package greenbrier.drinkmixer3000;

import android.os.Parcel;
import android.os.Parcelable;

/**
 * Created by McGiv on 8/30/2017.
 */

public class Drink implements Comparable<Drink>, Parcelable
{
    public final String name;
    public final boolean alcoholic;

    public static final Parcelable.Creator<Drink> CREATOR = new Parcelable.Creator<Drink>()
    {
        public Drink createFromParcel(Parcel in)
        {
            return new Drink(in);
        }

        public Drink[] newArray(int size)
        {
            return new Drink[size];
        }
    };



    public Drink(String name, boolean alc)
    {
        this.name = name;
        this.alcoholic = alc;
    }

    public Drink(Parcel in)
    {
        name = in.readString();
        alcoholic = in.readByte() == 1;
    }

    public int describeContents()
    {
        return 0;
    }

    public void writeToParcel(Parcel dest, int flags)
    {
        dest.writeString(name);
        if(alcoholic)
            dest.writeByte((byte)1);
        else
            dest.writeByte((byte)0);
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

    public String toString()
    {
        return name+":"+alcoholic;
    }



}
