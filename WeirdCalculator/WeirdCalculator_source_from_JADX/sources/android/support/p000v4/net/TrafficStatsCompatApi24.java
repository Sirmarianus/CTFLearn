package android.support.p000v4.net;

import android.annotation.TargetApi;
import android.net.TrafficStats;
import android.support.annotation.RequiresApi;
import android.support.annotation.RestrictTo;
import java.net.DatagramSocket;
import java.net.SocketException;

@TargetApi(24)
@RequiresApi(24)
@RestrictTo({RestrictTo.Scope.LIBRARY_GROUP})
/* renamed from: android.support.v4.net.TrafficStatsCompatApi24 */
public class TrafficStatsCompatApi24 {
    public static void tagDatagramSocket(DatagramSocket socket) throws SocketException {
        TrafficStats.tagDatagramSocket(socket);
    }

    public static void untagDatagramSocket(DatagramSocket socket) throws SocketException {
        TrafficStats.untagDatagramSocket(socket);
    }
}
