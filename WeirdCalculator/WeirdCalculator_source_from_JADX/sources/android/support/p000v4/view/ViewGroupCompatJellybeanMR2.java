package android.support.p000v4.view;

import android.annotation.TargetApi;
import android.support.annotation.RequiresApi;
import android.view.ViewGroup;

@TargetApi(18)
@RequiresApi(18)
/* renamed from: android.support.v4.view.ViewGroupCompatJellybeanMR2 */
class ViewGroupCompatJellybeanMR2 {
    ViewGroupCompatJellybeanMR2() {
    }

    public static int getLayoutMode(ViewGroup group) {
        return group.getLayoutMode();
    }

    public static void setLayoutMode(ViewGroup group, int mode) {
        group.setLayoutMode(mode);
    }
}
