package android.support.p000v4.p002os;

import android.os.Build;

/* renamed from: android.support.v4.os.BuildCompat */
public class BuildCompat {
    private BuildCompat() {
    }

    public static boolean isAtLeastN() {
        return Build.VERSION.SDK_INT >= 24;
    }

    public static boolean isAtLeastNMR1() {
        return Build.VERSION.SDK_INT >= 25;
    }

    public static boolean isAtLeastO() {
        return !"REL".equals(Build.VERSION.CODENAME) && ("O".equals(Build.VERSION.CODENAME) || Build.VERSION.CODENAME.startsWith("OMR"));
    }
}
