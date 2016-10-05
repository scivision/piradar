from numpy.fft import fftshift
from scipy.signal import spectrogram
from matplotlib.pyplot import figure,subplots
from matplotlib.colors import LogNorm

def spec(sig,Fs):
    f,t,Sxx = spectrogram(sig,fs=Fs)

    f = fftshift(f)
    Snorm = fftshift(Sxx/Sxx.max(),axes=0)

    fg,axs = subplots(2,1)
    fg.suptitle('$f_s$={} Hz'.format(Fs),y=0.99)

    ax = axs[0]
    h=ax.pcolormesh(t, f, Snorm,
                    cmap='viridis',norm=LogNorm(),vmin=1e-4)
    fg.colorbar(h,ax=ax).set_label('amplitude (normalized)')
    ax.set_ylabel('frequency [Hz]')
    ax.set_xlabel('time [sec]')
    ax.set_title('Spectrogram')
    ax.autoscale(True,'both',True)
#%%
    ax=axs[1]

    Savg = Snorm.mean(axis=1)
    Savg /= Savg.max()

    ax.semilogy(f,Savg)
    ax.set_ylabel('amplitude (normalized)')
    ax.set_xlabel('frequency [Hz]')
    ax.set_ylim(1e-4,None)
    ax.set_title('time-averaged spectrum')
    ax.autoscale(True,'x',True)


    fg.tight_layout()