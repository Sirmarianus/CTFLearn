package android.support.p000v4.view.animation;

import android.graphics.Path;
import android.os.Build;
import android.view.animation.Interpolator;

/* renamed from: android.support.v4.view.animation.PathInterpolatorCompat */
public final class PathInterpolatorCompat {
    private PathInterpolatorCompat() {
    }

    public static Interpolator create(Path path) {
        if (Build.VERSION.SDK_INT >= 21) {
            return PathInterpolatorCompatApi21.create(path);
        }
        return PathInterpolatorCompatBase.create(path);
    }

    public static Interpolator create(float controlX, float controlY) {
        if (Build.VERSION.SDK_INT >= 21) {
            return PathInterpolatorCompatApi21.create(controlX, controlY);
        }
        return PathInterpolatorCompatBase.create(controlX, controlY);
    }

    public static Interpolator create(float controlX1, float controlY1, float controlX2, float controlY2) {
        if (Build.VERSION.SDK_INT >= 21) {
            return PathInterpolatorCompatApi21.create(controlX1, controlY1, controlX2, controlY2);
        }
        return PathInterpolatorCompatBase.create(controlX1, controlY1, controlX2, controlY2);
    }
}
