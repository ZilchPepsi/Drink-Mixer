package greenbrier.drinkmixer3000

import android.support.v7.widget.RecyclerView
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView

/**
 * Created by emiller on 8/5/17.
 */
class CustomAdaptor(val drinkList: ArrayList<Drink>) : RecyclerView.Adapter<CustomAdaptor.ViewHolder>() {

    override fun onBindViewHolder(p0: ViewHolder?, p1: Int) {
        val drink: Drink = drinkList[p1]

        p0?.textViewName?.text = drink.name
        p0?.textViewAddress?.text = drink.address
    }

    override fun onCreateViewHolder(p0: ViewGroup?, p1: Int): ViewHolder {
        val v = LayoutInflater.from(p0?.context).inflate(R.layout.list_layout, p0, false)
        return ViewHolder(v)
    }

    override fun getItemCount(): Int {
        return drinkList.size
    }

    class ViewHolder(v: View) : RecyclerView.ViewHolder(v){
        val name = v
        val textViewName = itemView.findViewById(R.id.textViewName) as TextView
        val textViewAddress = itemView.findViewById(R.id.textViewAddress) as TextView
    }
}