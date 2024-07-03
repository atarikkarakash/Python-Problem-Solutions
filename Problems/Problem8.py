'''
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
'''

if __name__ == '__main__':
    # Kullanıcıdan giriş alınır ve tam sayıya dönüştürülür.
    # Bu sayı, kaç tane skorun girileceğini belirtir.
    n = int(input("Kaç skor girilecek? "))

    # Kullanıcıdan girilen skorlardan oluşan string bir girdi alınır,
    # bu girdi boşluklara göre bölünerek bir listeye dönüştürülür
    # ve her bir öğe tam sayıya dönüştürülür.
    arr = list(map(int, input("Skorları girin: ").split()))

    # Maksimum skoru buluruz.
    max_score = max(arr)
    
    # Maksimum skoru listeden kaldırırız.
    # Bu döngü, maksimum skoru birden fazla kez kaldırır
    # çünkü listede birden fazla maksimum skor olabilir.
    while max_score in arr:
        arr.remove(max_score)
    
    # İkinci en yüksek skoru (runner-up) buluruz.
    runner_up_score = max(arr)
    
    # İkinci en yüksek skoru yazdırırız.
    print("Runner-up score:", runner_up_score)
