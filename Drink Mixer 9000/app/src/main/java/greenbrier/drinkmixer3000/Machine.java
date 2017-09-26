package greenbrier.drinkmixer3000;

import android.os.Parcel;
import android.os.Parcelable;

/**
 * Created by McGiv on 9/25/2017.
 */

public class Machine implements Parcelable
{
    public static final int BAY_COUNT = 6;

    private Drink[] drinksList;

    public static final Parcelable.Creator<Machine> CREATOR = new Parcelable.Creator<Machine>()
    {
        public Machine createFromParcel(Parcel in)
        {
            return new Machine(in);
        }
        public Machine[] newArray(int size)
        {
            return new Machine[size];
        }
    };

    public Machine()
    {
        drinksList = new Drink[BAY_COUNT];
    }

    public Machine(Parcel in)
    {
        for(int x= 0; x< BAY_COUNT; x++)
            drinksList[x] = in.readParcelable(Drink.class.getClassLoader());
    }


    @Override
    public int describeContents() {
        return 0;
    }

    @Override
    public void writeToParcel(Parcel parcel, int i)
    {
        for(Drink d : drinksList)
        {
            parcel.writeParcelable(d, 0);
        }

    }

    public Drink[] getDrinks()
    {
        return drinksList;
    }

}
