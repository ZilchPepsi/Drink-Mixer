package greenbrier.drinkmixer3000

import android.os.Bundle
import android.support.design.widget.Snackbar
import android.support.v7.app.AppCompatActivity
import android.support.v7.widget.LinearLayoutManager
import android.support.v7.widget.RecyclerView
import android.view.Menu
import android.view.MenuItem
import android.widget.LinearLayout

import kotlinx.android.synthetic.main.activity_main.*
import kotlinx.android.synthetic.main.content_main.*

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        setSupportActionBar(toolbar)

        fab.setOnClickListener { view ->
            Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                    .setAction("Action", null).show()
        }

        recyclerView.layoutManager = LinearLayoutManager(this, LinearLayout.VERTICAL,false)

        val drinks = ArrayList<Drink>()

        drinks.add(Drink("Cuba Libre", "Coca-Cola, lime, and dark or light rum."))
        drinks.add(Drink("Mojito", "White rum, sugar, lime juice, soda water, and mint."))
        drinks.add(Drink("Long Island Iced Tea", "1/2 ounce triple sec\n" +
                                                                    "1/2 ounce light rum\n" +
                                                                    "1/2 ounce gin\n" +
                                                                    "1/2 ounce vodka\n" +
                                                                    "1/2 ounce tequila\n" +
                                                                    "1-ounce sour mix\n" +
                                                                    "Cola\n" +
                                                                    "Lemon wedge for garnish "))
        drinks.add(Drink("Cosmopolitan","1/2 oz Fresh lime juice, 1 oz Cranberry juice, 1/2 oz Cointreau, 1 1/2 oz Vodka Citron"))
        drinks.add(Drink("Mai Tai", "1 1/2 oz White rum, 1/2 oz Fresh lime juice, 1/2 oz Orange curaçao, 1/2 oz Orgeat syrup, 3/4 oz Dark rum"))

        val adapter = CustomAdaptor(drinks)

        recyclerView.adapter = adapter
    }

    override fun onCreateOptionsMenu(menu: Menu): Boolean {
        // Inflate the menu; this adds items to the action bar if it is present.
        menuInflater.inflate(R.menu.menu_main, menu)
        return true
    }

    override fun onOptionsItemSelected(item: MenuItem): Boolean {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        return when (item.itemId) {
            R.id.action_settings -> true
            else -> super.onOptionsItemSelected(item)
        }
    }
}