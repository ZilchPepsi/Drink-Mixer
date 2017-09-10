package greenbrier.drinkmixer3000;

import java.util.ArrayList;

/**
 * Created by McGiv on 9/9/2017.
 */

public class WorkOrder
{
    public final  int order;
    public final  ArrayList<Object> data;

    public WorkOrder(int order, Object... data)
    {
        this.order = order;
        this.data = new ArrayList<Object>();
            for(Object o : data)
                this.data.add(o);
    }
}
