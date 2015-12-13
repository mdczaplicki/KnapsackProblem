#include "knapsackproblem.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    KnapsackProblem w;
    w.show();

    return a.exec();
}
