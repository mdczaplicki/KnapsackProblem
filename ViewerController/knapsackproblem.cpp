#include "knapsackproblem.h"
#include "ui_knapsackproblem.h"

KnapsackProblem::KnapsackProblem(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::KnapsackProblem)
{
    ui->setupUi(this);
}

KnapsackProblem::~KnapsackProblem()
{
    delete ui;
}

void KnapsackProblem::on_eval_button_clicked()
{

}
