
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
namespace Logi_Gui
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {



        }

    private void load_button_Click(object sender, EventArgs e)
    {
        lista.Items.Clear();
        string connStr = "server=localhost;user=toor;database=skany_base;password=ZAQ!2wsx";
        MySqlConnection conn = new MySqlConnection(connStr);
        try
        {
            conn.Open();
            string sql = "SELECT s.ip,s.kod,a.indeks,s.data,a.nazwa,s.blad FROM skany s left join artykul a on a.idartykul = s.idartykul"; // Use your table name here
            MySqlCommand cmd = new MySqlCommand(sql, conn);
            MySqlDataReader rdr = cmd.ExecuteReader();
    
            var items = new List<Item>();
            while (rdr.Read())
            {
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
            rdr.Close();
    
            foreach(var item in items)
            {
                ListViewItem listItem = new ListViewItem(new[] {item.ip, item.kod, item.indeks,item.data,item.nazwa,item.blad});
                lista.Items.Add(listItem);
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine(ex.ToString());
        }
        conn.Close();
    }

    //Create Item class to hold JSON Data
    public class Item
    {
        public string ip { get; set; }
        public string kod { get; set; }
        public string indeks { get; set; }
        public string data { get; set; }
        public string nazwa { get; set; }
        public string blad { get; set; }



        }

        private void lista_SelectedIndexChanged(object sender, EventArgs e)
        {

        }
    }
}
