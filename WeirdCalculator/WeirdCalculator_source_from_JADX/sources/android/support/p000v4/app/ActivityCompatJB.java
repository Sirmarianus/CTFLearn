package android.support.p000v4.app;

import android.annotation.TargetApi;
import android.app.Activity;
import android.content.Intent;
import android.content.IntentSender;
import android.os.Bundle;
import android.support.annotation.RequiresApi;

@TargetApi(16)
@RequiresApi(16)
/* renamed from: android.support.v4.app.ActivityCompatJB */
class ActivityCompatJB {
    ActivityCompatJB() {
    }

    public static void startActivityForResult(Activity activity, Intent intent, int requestCode, Bundle options) {
        activity.startActivityForResult(intent, requestCode, options);
    }

    public static void startIntentSenderForResult(Activity activity, IntentSender intent, int requestCode, Intent fillInIntent, int flagsMask, int flagsValues, int extraFlags, Bundle options) throws IntentSender.SendIntentException {
        activity.startIntentSenderForResult(intent, requestCode, fillInIntent, flagsMask, flagsValues, extraFlags, options);
    }

    public static void finishAffinity(Activity activity) {
        activity.finishAffinity();
    }
}
