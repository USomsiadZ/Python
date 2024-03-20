
// Importowanie niezbędnych bibliotek
using MySql.Data.MySqlClient;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Newtonsoft.Json;

// Deklaracja przestrzeni nazw
namespace Logi_Gui
{
    // Definicja klasy Form1
    public partial class Form1 : Form
    {
        // Konstruktor klasy Form1
        public Form1()
        {
            // Inicjalizacja komponentów interfejsu użytkownika
            InitializeComponent();
        }

        // Metoda wywoływana podczas ładowania formularza
        // Metoda wywoływana po kliknięciu przycisku load_button
        private void load_button_Click(object sender, EventArgs e)
        {
            // Czyszczenie listy przed dodaniem nowych elementów
            lista.Items.Clear();

            // Dane do połączenia z bazą danych
            string connStr = "server=localhost;user=toor;database=skany_base;password=ZAQ!2wsx";

            // Utworzenie nowego połączenia z bazą danych
            MySqlConnection conn = new MySqlConnection(connStr);

            try
            {
                // Otwarcie połączenia z bazą danych
                conn.Open();

                // Zapytanie SQL do bazy danych
                string sql = "SELECT s.ip,s.kod,a.indeks,s.data,a.nazwa,s.blad FROM skany s left join artykul a on a.idartykul = s.idartykul";

                // Utworzenie nowego polecenia SQL
                MySqlCommand cmd = new MySqlCommand(sql, conn);

                // Wykonanie polecenia SQL i przechowanie wyników w MySqlDataReader
                MySqlDataReader rdr = cmd.ExecuteReader();

                // Utworzenie nowej listy obiektów typu Item
                var items = new List<Item>();

                // Pętla przez wszystkie wyniki zapytania SQL
                while (rdr.Read())
                {
                    // Dodawanie każdego wyniku do listy obiektów typu Item
                    items.Add(new Item()
                    {
                        ip = rdr["ip"] == DBNull.Value ? null : rdr["ip"].ToString(),
                        kod = rdr["kod"] == DBNull.Value ? null : rdr["kod"].ToString(),
                        indeks = rdr["indeks"] == DBNull.Value ? null : rdr["indeks"].ToString(),
                        data = rdr["data"] == DBNull.Value ? null : rdr["data"].ToString(),
                        nazwa = rdr["nazwa"] == DBNull.Value ? null : rdr["nazwa"].ToString(),
                        blad = rdr[5].ToString(),
                    });
                }

                // Zamknięcie MySqlDataReader
                rdr.Close();

                // Pętla przez wszystkie obiekty typu Item
                foreach (var item in items)
                {
                    // Utworzenie nowego obiektu ListViewItem i dodanie go do listy
                    ListViewItem listItem = new ListViewItem(new[] { item.ip, item.kod, item.indeks, item.data, item.nazwa, item.blad });
                    lista.Items.Add(listItem);
                }
            }
            catch (Exception ex)
            {
                // Wyświetlenie informacji o ewentualnym wyjątku
                Console.WriteLine(ex.ToString());
            }

            // Zamknięcie połączenia z bazą danych
            conn.Close();
        }

        // Definicja klasy Item do przechowywania danych JSON
        public class Item
        {
            public string ip { get; set; }
            public string kod { get; set; }
            public string indeks { get; set; }
            public string data { get; set; }
            public string nazwa { get; set; }
            public string blad { get; set; }
        }


    }
}
