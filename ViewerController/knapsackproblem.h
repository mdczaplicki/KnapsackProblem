#ifndef KNAPSACKPROBLEM_H
#define KNAPSACKPROBLEM_H

#include <QMainWindow>

namespace Ui {
class KnapsackProblem;
}

class KnapsackProblem : public QMainWindow
{
    Q_OBJECT

public:
    explicit KnapsackProblem(QWidget *parent = 0);
    ~KnapsackProblem();

private slots:
    void on_eval_button_clicked();

private:
    Ui::KnapsackProblem *ui;
};

#endif // KNAPSACKPROBLEM_H
