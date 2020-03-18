import pandas as pd
import matplotlib.pyplot as plt

dataframe = pd.read_csv("test1.csv")
x = dataframe.numThreads
y= dataframe.runtime1

x1 = dataframe.numThreads
y1= dataframe.runtime2

x2 = dataframe.numThreads
y2= dataframe.runtime3

x3 = dataframe.numThreads
y3= dataframe.runtime4

x4 = dataframe.numThreads
y4= dataframe.runtime5

x5 = dataframe.numThreads
y5= dataframe.runtime6


x6 = dataframe.numThreads
y6= dataframe.runtime7

x7 = dataframe.numThreads
y7= dataframe.runtime8

x8 = dataframe.numThreads
y8= dataframe.runtime9
x9 = dataframe.numThreads
y9= dataframe.runtime10

fig1=plt.figure(1)
plt.plot(x, y)
fig2=plt.figure(2)
plt.plot(x1, y1)
fig3=plt.figure(3)
plt.plot(x2, y2)
fig4=plt.figure(4)
plt.plot(x3, y3)
fig5=plt.figure(5)
plt.plot(x4, y4)
fig6=plt.figure(6)
plt.plot(x5, y5)
fig7=plt.figure(7)
plt.plot(x6, y6)
fig8=plt.figure(8)
plt.plot(x7, y7)
fig9=plt.figure(9)
plt.plot(x8, y8)
fig10=plt.figure(10)
plt.plot(x9, y9)
fig1.suptitle('the relation between run-time and number of threads for N equals 100 ', fontsize=14, fontweight='bold')
fig2.suptitle('the relation between run-time and number of threads for N equals 300', fontsize=14, fontweight='bold')
fig3.suptitle('the relation between run-time and number of threads for N equals 500', fontsize=14, fontweight='bold')
fig4.suptitle('the relation between run-time and number of threads for N equals 900', fontsize=14, fontweight='bold')
fig5.suptitle('the relation between run-time and number of threads for N equals 1100', fontsize=14, fontweight='bold')
fig6.suptitle('the relation between run-time and number of threads for N equals 1300', fontsize=14, fontweight='bold')
fig7.suptitle('the relation between run-time and number of threads for N equals 1500', fontsize=14, fontweight='bold')
fig8.suptitle('the relation between run-time and number of threads for N equals 1700', fontsize=14, fontweight='bold')
fig9.suptitle('the relation between run-time and number of threads for N equals 1900', fontsize=14, fontweight='bold')
fig10.suptitle('the relation between run-time and number of threads for N equals 700', fontsize=14, fontweight='bold')

ax1 = fig1.add_subplot(111)
ax1.set_xlabel('numThreads')
ax1.set_ylabel('Run-time')
ax2 = fig2.add_subplot(111)
ax2.set_xlabel('numThreads')
ax2.set_ylabel('Run-time')
ax3 = fig3.add_subplot(111)
ax3.set_xlabel('numThreads')
ax3.set_ylabel('Run-time')
ax4 = fig4.add_subplot(111)
ax4.set_xlabel('numThreads')
ax4.set_ylabel('Run-time')
ax5 = fig5.add_subplot(111)
ax5.set_xlabel('numThreads')
ax5.set_ylabel('Run-time')
ax6 = fig6.add_subplot(111)
ax6.set_xlabel('numThreads')
ax6.set_ylabel('Run-time')
ax7 = fig7.add_subplot(111)
ax7.set_xlabel('numThreads')
ax7.set_ylabel('Run-time')
ax8 = fig8.add_subplot(111)
ax8.set_xlabel('numThreads')
ax8.set_ylabel('Run-time')
ax9 = fig9.add_subplot(111)
ax9.set_xlabel('numThreads')
ax9.set_ylabel('Run-time')
ax10 = fig10.add_subplot(111)
ax10.set_xlabel('numThreads')
ax10.set_ylabel('Run-time')
fig1.savefig("1.png")
fig2.savefig("2.png")
fig3.savefig("3.png")
fig4.savefig("4.png")
fig5.savefig("5.png")
fig6.savefig("6.png")
fig7.savefig("7.png")
fig8.savefig("8.png")
fig9.savefig("9.png")
fig10.savefig("10.png")

#plt.show()  