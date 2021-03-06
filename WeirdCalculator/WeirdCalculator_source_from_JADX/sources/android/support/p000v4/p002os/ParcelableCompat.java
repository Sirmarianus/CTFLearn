package android.support.p000v4.p002os;

import android.os.Build;
import android.os.Parcel;
import android.os.Parcelable;

/* renamed from: android.support.v4.os.ParcelableCompat */
public final class ParcelableCompat {
    public static <T> Parcelable.Creator<T> newCreator(ParcelableCompatCreatorCallbacks<T> callbacks) {
        if (Build.VERSION.SDK_INT >= 13) {
            return ParcelableCompatCreatorHoneycombMR2Stub.instantiate(callbacks);
        }
        return new CompatCreator(callbacks);
    }

    /* renamed from: android.support.v4.os.ParcelableCompat$CompatCreator */
    static class CompatCreator<T> implements Parcelable.Creator<T> {
        final ParcelableCompatCreatorCallbacks<T> mCallbacks;

        public CompatCreator(ParcelableCompatCreatorCallbacks<T> callbacks) {
            this.mCallbacks = callbacks;
        }

        public T createFromParcel(Parcel source) {
            return this.mCallbacks.createFromParcel(source, (ClassLoader) null);
        }

        public T[] newArray(int size) {
            return this.mCallbacks.newArray(size);
        }
    }

    private ParcelableCompat() {
    }
}
