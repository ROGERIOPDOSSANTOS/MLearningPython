{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# <font color='blue'>Machine Learning</font>\n",
    "\n",
    "# <font color='blue'>Regressão</font>"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Parte 1: Código para a fórmula básica da regressão linear simples e calculo de coeficientes. \n",
    "\n",
    "Parte 2: Modelo de previsões."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "O dataset abaixo contém dados sobre..."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Imports\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import statsmodels.formula.api as smf"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>ano</th>\n",
       "      <th>mes</th>\n",
       "      <th>chuva</th>\n",
       "      <th>evaporacao</th>\n",
       "      <th>insolacao</th>\n",
       "      <th>tempmed</th>\n",
       "      <th>umidrel</th>\n",
       "      <th>tempmax_abs</th>\n",
       "      <th>tempmax_med</th>\n",
       "      <th>tempmin_abs</th>\n",
       "      <th>tempmin_med</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1975.0</td>\n",
       "      <td>1.0</td>\n",
       "      <td>136.0</td>\n",
       "      <td>134.9</td>\n",
       "      <td>224.7</td>\n",
       "      <td>24.2</td>\n",
       "      <td>70.9</td>\n",
       "      <td>34.4</td>\n",
       "      <td>30.7</td>\n",
       "      <td>14.6</td>\n",
       "      <td>18.9</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1975.0</td>\n",
       "      <td>2.0</td>\n",
       "      <td>242.9</td>\n",
       "      <td>104.4</td>\n",
       "      <td>195.3</td>\n",
       "      <td>25.3</td>\n",
       "      <td>76.9</td>\n",
       "      <td>36.2</td>\n",
       "      <td>30.4</td>\n",
       "      <td>16.8</td>\n",
       "      <td>21.1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1975.0</td>\n",
       "      <td>3.0</td>\n",
       "      <td>125.1</td>\n",
       "      <td>101.1</td>\n",
       "      <td>192.8</td>\n",
       "      <td>23.9</td>\n",
       "      <td>79.1</td>\n",
       "      <td>33.7</td>\n",
       "      <td>29.9</td>\n",
       "      <td>17.3</td>\n",
       "      <td>19.7</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1975.0</td>\n",
       "      <td>4.0</td>\n",
       "      <td>98.9</td>\n",
       "      <td>156.8</td>\n",
       "      <td>201.5</td>\n",
       "      <td>21.0</td>\n",
       "      <td>75.0</td>\n",
       "      <td>30.6</td>\n",
       "      <td>26.8</td>\n",
       "      <td>13.4</td>\n",
       "      <td>16.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1975.0</td>\n",
       "      <td>5.0</td>\n",
       "      <td>66.3</td>\n",
       "      <td>95.5</td>\n",
       "      <td>203.6</td>\n",
       "      <td>18.1</td>\n",
       "      <td>72.1</td>\n",
       "      <td>29.0</td>\n",
       "      <td>23.8</td>\n",
       "      <td>9.0</td>\n",
       "      <td>14.3</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      ano  mes  chuva  evaporacao  insolacao  tempmed  umidrel  tempmax_abs  \\\n",
       "0  1975.0  1.0  136.0       134.9      224.7     24.2     70.9         34.4   \n",
       "1  1975.0  2.0  242.9       104.4      195.3     25.3     76.9         36.2   \n",
       "2  1975.0  3.0  125.1       101.1      192.8     23.9     79.1         33.7   \n",
       "3  1975.0  4.0   98.9       156.8      201.5     21.0     75.0         30.6   \n",
       "4  1975.0  5.0   66.3        95.5      203.6     18.1     72.1         29.0   \n",
       "\n",
       "   tempmax_med  tempmin_abs  tempmin_med  \n",
       "0         30.7         14.6         18.9  \n",
       "1         30.4         16.8         21.1  \n",
       "2         29.9         17.3         19.7  \n",
       "3         26.8         13.4         16.8  \n",
       "4         23.8          9.0         14.3  "
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Carregando o dataset\n",
    "df = pd.read_csv('dados/dados1975-2015.csv')\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Definindo variáveis x e y\n",
    "X = df['ano'].values\n",
    "Y = df['chuva'].values"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "#Chamando a Função e mostrando o grafico \n",
    "plt.scatter(X,Y)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(X,Y)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                            OLS Regression Results                            \n",
      "==============================================================================\n",
      "Dep. Variable:            tempmax_abs   R-squared:                       0.451\n",
      "Model:                            OLS   Adj. R-squared:                  0.450\n",
      "Method:                 Least Squares   F-statistic:                     402.7\n",
      "Date:                Mon, 13 Dec 2021   Prob (F-statistic):           8.07e-66\n",
      "Time:                        08:14:05   Log-Likelihood:                -1064.4\n",
      "No. Observations:                 492   AIC:                             2133.\n",
      "Df Residuals:                     490   BIC:                             2141.\n",
      "Df Model:                           1                                         \n",
      "Covariance Type:            nonrobust                                         \n",
      "===============================================================================\n",
      "                  coef    std err          t      P>|t|      [0.025      0.975]\n",
      "-------------------------------------------------------------------------------\n",
      "Intercept      29.5468      0.191    154.444      0.000      29.171      29.923\n",
      "tempmin_abs     0.3342      0.017     20.067      0.000       0.301       0.367\n",
      "==============================================================================\n",
      "Omnibus:                        1.107   Durbin-Watson:                   1.168\n",
      "Prob(Omnibus):                  0.575   Jarque-Bera (JB):                0.922\n",
      "Skew:                           0.089   Prob(JB):                        0.631\n",
      "Kurtosis:                       3.115   Cond. No.                         23.2\n",
      "==============================================================================\n",
      "\n",
      "Notes:\n",
      "[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.\n"
     ]
    }
   ],
   "source": [
    "# Criando o Modelo de Regressão\n",
    "estimativa = smf.ols(formula = 'tempmax_abs ~ tempmin_abs', data = df)\n",
    "\n",
    "# Treinando o Modelo de Regressão\n",
    "modelo = estimativa.fit()\n",
    "\n",
    "# Imprimindo o resumo do modelo\n",
    "print(modelo.summary())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "collapsed": true
   },
   "source": [
    "# Fim"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Obrigado "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}