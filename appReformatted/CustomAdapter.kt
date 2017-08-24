package greenbrier.drinkmixer3000


import android.annotation.SuppressLint
import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import kotlinx.android.synthetic.main.activity_main.*
import org.w3c.dom.Text
import java.lang.reflect.Type

/**
 * Created by EMiller on 8/21/2017.
 *
 */

 
 
class CustomAdapter(val drinkList: ArrayList<Drink>) : RecyclerView.Adapter<CustomAdapter.ViewHolder>() {

    //this method is returning the view for each item in the list
    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): CustomAdapter.ViewHolder {
        val v = LayoutInflater.from(parent.context).inflate(R.layout.list_layout, parent, false)
        return ViewHolder(v)
    }

    //this method is binding the data on the list
    override fun onBindViewHolder(holder: CustomAdapter.ViewHolder, position: Int) {
        holder.bindItems(drinkList[position])
    }

    //this method is giving the size of the list
    override fun getItemCount(): Int {
        return drinkList.size
    }

    //the class is holding the list view
    class ViewHolder(itemView: View) : RecyclerView.ViewHolder(itemView) {

        fun bindItems(drink: Drink) {
            val textViewDrink = itemView.findViewById<View>(R.id.textViewDrink) as TextView
            val textViewRecipe  = itemView.findViewById<View>(R.id.textViewRecipe) as TextView
            textViewDrink.text = drink.name
            textViewRecipe.text = drink.recipe
        }
    }
}