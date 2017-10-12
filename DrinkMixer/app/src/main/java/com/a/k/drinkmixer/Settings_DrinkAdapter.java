package com.a.k.drinkmixer;

import android.support.v7.widget.RecyclerView;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import java.util.ArrayList;

/**
 * Created by McGiv on 9/25/2017.
 */

public class Settings_DrinkAdapter extends RecyclerView.Adapter<Settings_DrinkAdapter.CustomViewHolder>
{
    private ArrayList<Drink> drinks;

    public Settings_DrinkAdapter(ArrayList<Drink> d)
    {
        drinks = d;
    }

    @Override
    public Settings_DrinkAdapter.CustomViewHolder onCreateViewHolder(ViewGroup parent, int viewType)
    {
        View v = LayoutInflater.from(parent.getContext()).inflate(R.layout.settings_drink_layout, parent, false);
        return new Settings_DrinkAdapter.CustomViewHolder(v);
    }

    @Override
    public void onBindViewHolder(CustomViewHolder holder, int position)
    {
        holder.bindItems(drinks.get(position));
    }

    @Override
    public int getItemCount()
    {
        return drinks.size();
    }


    class CustomViewHolder extends RecyclerView.ViewHolder
    {
        public CustomViewHolder(View itemView)
        {
            super(itemView);
        }

        public void bindItems(Drink d)
        {
            TextView textViewDrink = itemView.findViewById(R.id.textViewDrink);

            textViewDrink.setText(d.name);
        }
    }


}
