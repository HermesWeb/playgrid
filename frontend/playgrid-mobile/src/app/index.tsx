import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';

export default function App() {
  return (
    <SafeAreaView style={styles.container}>
      <StatusBar style="light" />
      
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.logoText}>Play<Text style={styles.neonText}>Grid</Text></Text>
        <Text style={styles.subText}>Find your next game</Text>
      </View>

      {/* Turf Card */}
      <View style={styles.card}>
        <Text style={styles.cardTitle}>Campus Mini-Stadium</Text>
        <Text style={styles.cardLocation}>Akoka</Text>
        
        <View style={styles.cardFooter}>
          <Text style={styles.price}>₦25,000 / hr</Text>
          <TouchableOpacity style={styles.bookButton}>
            <Text style={styles.bookButtonText}>Book Now</Text>
          </TouchableOpacity>
        </View>
      </View>

    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#121212',
    paddingTop: 40,
    paddingHorizontal: 20,
  },
  header: {
    marginBottom: 30,
  },
  logoText: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#FFFFFF',
  },
  neonText: {
    color: '#39FF14',
  },
  subText: {
    color: '#888888',
    fontSize: 16,
    marginTop: 5,
  },
  card: {
    backgroundColor: '#1E1E1E',
    padding: 20,
    borderRadius: 15,
    borderWidth: 1,
    borderColor: '#333333',
  },
  cardTitle: {
    color: '#FFFFFF',
    fontSize: 20,
    fontWeight: 'bold',
  },
  cardLocation: {
    color: '#AAAAAA',
    fontSize: 14,
    marginTop: 5,
    marginBottom: 15,
  },
  cardFooter: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
  },
  price: {
    color: '#39FF14',
    fontSize: 18,
    fontWeight: 'bold',
  },
  bookButton: {
    backgroundColor: '#39FF14',
    paddingVertical: 10,
    paddingHorizontal: 20,
    borderRadius: 8,
  },
  bookButtonText: {
    color: '#121212',
    fontWeight: 'bold',
    fontSize: 16,
  }
});