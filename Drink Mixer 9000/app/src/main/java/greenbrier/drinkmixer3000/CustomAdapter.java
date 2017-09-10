package greenbrier.drinkmixer3000;

import android.support.v7.widget.RecyclerView;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by McGiv on 8/31/2017.
 */

public class CustomAdapter extends RecyclerView.Adapter<CustomAdapter.CustomViewHolder>
{
    private ArrayList<Mix> mixes;
    private ArrayList<Drink> drinks;

    public CustomAdapter(ArrayList<Drink> d, ArrayList<Mix> m)
    {
        drinks = d;
        mixes = m;
    }


    public boolean addDrink(Drink d)
    {
        if (!drinks.contains(d))
        {
            drinks.add(d);
            return true;
        }
        return false;

    }

    public boolean addMix(Mix m)
    {
        if(!mixes.contains(m))
        {
            mixes.add(m);
            return true;
        }
        return false;
    }

    public Drink getDrink(String name)
    {
        for(int x =0; x< drinks.size(); x++)
            if(drinks.get(x).name.equals(name))
                return drinks.get(x);
        return null;
    }





    @Override
    public CustomViewHolder onCreateViewHolder(ViewGroup parent, int viewType)
    {
        View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.list_layout, parent, false);
        return new CustomAdapter.CustomViewHolder(v);
    }



    @Override
    public void onBindViewHolder(CustomViewHolder holder, int position)
    {
        holder.bindItems(mixes.get(position));
    }

    @Override
    public int getItemCount()
    {
        return mixes.size();
    }

    class CustomViewHolder extends RecyclerView.ViewHolder
    {
        public CustomViewHolder(View itemView)
        {
            super(itemView);
        }

        public void bindItems(Mix m)
        {
            TextView textViewDrink = (TextView) itemView.findViewById(R.id.textViewDrink);
            TextView textViewRecipe = (TextView) itemView.findViewById(R.id.textViewRecipe);
            textViewDrink.setText(m.getName());

            for(Drink d :m.getDrinks().keySet())
            {
                textViewRecipe.append(d.name + " " +m.getDrinks().get(d)+"\n");
            }

        }
    }
}